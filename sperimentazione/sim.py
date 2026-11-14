import numpy as np
rng=np.random.default_rng(42)
DT=5                      # minuti per passo
T0,T1=6*60,11*60+30       # 6:00 - 11:30
steps=(T1-T0)//DT
import json, os
P=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','dati','parametri.json')))
N=P['auto_tratto_chiuso_6_10']['valore']
# orari di partenza desiderati: triangolare 6:00-10:00, picco 7:30
des=rng.triangular(6*60,7*60+30,10*60,N)
CAP={'cap':P['capacita_rampa_auto_ora']['valore'],'vom':P['capacita_rampa_auto_ora']['valore']}
METRO=P['metro_l1_auto_assorbite_ora']['valore']
def queue(arr,caph):
    srv=caph*DT/60; q=0; Q=[];W=0
    for a in arr:
        q=max(0,q+a-srv); Q.append(q); W+=q*DT/60
    return np.array(Q),W
def hist(times):
    idx=((np.array(times)-T0)//DT).astype(int); idx=idx[(idx>=0)&(idx<steps)]
    return np.bincount(idx,minlength=steps).astype(float)
EXTRA=[0]
def run(scen,adopt=0.0,follow=0.7):
    EXTRA[0]=0
    users=rng.random(N)<adopt
    arr={'cap':np.zeros(steps),'vom':np.zeros(steps)}
    if scen=='A':
        g=rng.random(N)<0.8                     # senza avviso: 80% all'ultima uscita, 20% devia col navigatore
        arr['cap']+=hist(des[g]); arr['vom']+=hist(des[~g])
    elif scen=='B':
        f=rng.random(N)<follow
        arr['vom']+=hist(des[f]); arr['cap']+=hist(des[~f])
    else:
        nu=des[~users]; g=rng.random(len(nu))<0.8   # chi non usa Jammo: come oggi
        arr['cap']+=hist(nu[g]); arr['vom']+=hist(nu[~g])
        # capacità per passo lasciata agli utenti: 85% (15% libero), meno i non utenti previsti
        free={k:np.maximum(0,np.full(steps,CAP[k]*DT/60*(1-P['quota_libera_non_utenti']['valore']))-arr[k]) for k in CAP}
        free['met']=np.full(steps,METRO*DT/60)
        pen={'cap':0,'vom':5,'met':10}
        for t in np.sort(des[users]):
            i=int((t-T0)//DT); best=None
            for sh in range(0,13):              # spostare la partenza fino a 60 min
                j=i+sh
                if j>=steps: break
                for k in ('cap','vom','met'):
                    if free[k][j]>=1:
                        c=sh*DT+pen[k]
                        if best is None or c<best[0]: best=(c,k,j)
                if best and best[0]<=sh*DT: break
            if best is None: arr['cap'][min(i,steps-1)]+=1; continue
            c,k,j=best; free[k][j]-=1; EXTRA[0]+=c
            if k!='met': arr[k][j]+=1
    extra=0
    if scen=='C':
        extra=EXTRA[0]/60
    tot=np.zeros(steps); W=extra
    for k in ('cap','vom'):
        Q,w=queue(arr[k],CAP[k]); tot+=Q; W+=w
    return tot,W
QA,WA=run('A'); QB,WB=run('B')
print('A picco auto in coda %d, ore perse %d, min medi %.0f'%(QA.max(),WA,WA*60/N))
print('B picco %d, ore %d, min %.0f'%(QB.max(),WB,WB*60/N))
res={}
for ad in (0.2,0.35,0.5):
    QC,WC=run('C',ad); res[ad]=(QC,WC)
    print('C adoz %.0f%%: picco %d (-%d%%), ore %d (-%d%%), min %.0f'%(ad*100,QC.max(),100-100*QC.max()/QA.max(),WC,100-100*WC/WA,WC*60/N))

