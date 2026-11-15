LIVE DEMO : <br>
https://davencode.github.io/jammo/Jammo_liveDemo.html#casa

IL PROBLEMA <br>
A Napoli una strada chiusa la scopri quando ci sei già dentro. Gli avvisi ufficiali arrivano tardi e sono uguali per tutti, così il navigatore manda migliaia di persone sulla stessa alternativa e la coda, invece di sparire, si sposta. Succede con i cantieri, gli scioperi, i concerti e le partite, le navi da crociera, le allerte meteo e le scosse ai Campi Flegrei.

LA SOLUZIONE <br>
**Jammo** è l'assistente della città. Mette insieme servizi che oggi sono separati (trasporti pubblici, strade e parcheggi, biglietti, eventi, turismo e avvisi ufficiali) e li trasforma in un unico piano, su misura per ciascuno. Ogni servizio ha il suo agente (mobilità, turismo, eventi, rete) e gli agenti si coordinano tra loro: invece di dieci app e dieci avvisi, ricevi una sola indicazione.

Ogni giorno Jammo ti dice quando partire e con quale mezzo, ti indica dove parcheggiare e ti avvisa di scioperi e cantieri. Quando qualcosa blocca la città, lo stesso sistema fa la differenza in tre mosse:
1. Sa in anticipo. Chi usa l'app indica a che ora parte e dove va, senza dare il proprio nome. Così sa prima quante persone si sposteranno, e dove.
2. Assegna, invece di consigliare. Distribuisce le persone su strade, fasce orarie e mezzi senza superare quello che possono reggere, e lascia sempre una quota libera per chi non usa l'app.
3. Prepara tutto quando la città è tranquilla. Il piano arriva sul telefono in anticipo, e nel momento critico basta un messaggio breve.

Con gli eventi prevedibili gioca d'anticipo: dopo un concerto scagliona le uscite, indica a ciascuno parcheggio e percorso a piedi e chiede corse in più dei treni. Con gli imprevisti conta il piano di riserva già sul telefono.

ALCUNI ESEMPI
- Lavori in Tangenziale, noti la sera prima. Arriva una notifica, esempio: «Parti alle 7, esci dalla Tangenziale al Vomero e arrivi alla stessa ora». A un'altra persona viene assegnata un'altra fascia oraria oppure la metro.
- La scossa del 31 luglio 2026. I treni si fermano e la rete rallenta, ma il piano di riserva è già sul telefono: ognuno legge la propria istruzione. Jammo non prevede i terremoti: porta a ciascuno le istruzioni ufficiali.
- Le navi da crociera. La regia fa partire i pullman delle escursioni mezz'ora dopo, e le strade del porto restano libere per chi lavora.

CHIAMATE E SMS <br>
Jammo raggiunge qualsiasi telefono, anche senza app.
- Chiamata: una normale telefonata all'assistente vocale, che conosce già il tuo piano e ti spiega a voce cosa fare. Va bene per un anziano come per un turista;
- SMS: funziona anche senza internet. Jammo lo usa in tre momenti: la sera prima, per mandare il piano a chi non ha l'app; durante un'emergenza, per dire a ciascuno cosa fare; dopo una chiamata all'assistente, per riassumere le indicazioni. Il biglietto si compra cliccando il link o rispondendo all'SMS e pagando con il credito telefonico (rispondendo «1» confermi che prenderai quel mezzo, con «2» dici che non puoi e il tuo posto passa a un'altra persona);
- Messaggio di zona: un unico messaggio a tutti i telefoni di una zona.

COME DECIDE E CHI CONTROLLA <br>
L'AI lavora in quattro passi: **raccoglie** i dati, **prevede** quante persone si muoveranno e dove, le **assegna** entro le capienze e scrive a ciascuno il suo messaggio. I numeri li fa la matematica, le parole l'AI e le scelte una persona.
Le decisioni sono su tre livelli:
- Automatiche, anche migliaia per evento: assegnarti l'uscita Vomero, spostarti su un altro treno se salta il tuo, mandarti l'SMS, rispondere alla tua chiamata. Le prende il sistema, dentro regole fissate.
- Piani già approvati, pochi e scritti una volta: «se la Tangenziale chiude, apri queste alternative con queste capienze»; «se la scossa supera una certa soglia, attiva il piano di riserva». Si approvano giorni prima, poi partono da soli.
- Decisioni umane, poche decine al massimo: chiudere una strada, deviare una linea, chiedere treni in più, mandare un messaggio a tutta una zona. Le prende l'operatore, con un clic.
Ogni decisione resta registrata con il suo perché.

DATI REALI E SIMULATI <br>
Il prototipo usa dati reali dove sono pubblici: il traffico della Tangenziale (circa 270.000 transiti al giorno), gli orari di metro e bus dal feed GTFS di ANM, la scossa del 31 luglio dai dati INGV, il traffico crocieristico del porto (circa 1,85 milioni di passeggeri nel 2025). Simula invece ciò che richiede accordi: auto per rampa, presenze dalla rete mobile, ingressi ai tornelli, prenotazioni turistiche, orari e destinazioni degli utenti. Non servono dati in tempo reale: le stime si fanno prima. Fonti e parametri sono nel repository.

RISULTATO IN SIMULAZIONE <br>
Nel modello (9.800 auto sul tratto chiuso, due rampe e la metro), se una persona su tre usa Jammo la coda nel momento peggiore si riduce di circa il **70%**. Dare a tutti lo stesso consiglio, invece, sposta soltanto la coda.
