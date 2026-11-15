# Dati usati da Jammo

Il prototipo usa **dati reali** dove sono pubblici, i **sensori IoT già installati in strada** e **dati simulati** dove servirebbero accordi con aziende ed enti. Ogni parametro della simulazione è in `parametri.json`, con il tipo (reale, simulato o ipotesi) e la fonte.

## Dati reali
| Dato | Valore | Fonte |
|---|---|---|
| Traffico in Tangenziale | circa 270.000 transiti al giorno | Tangenziale di Napoli SpA, via [Telepass](https://www.telepass.com/it/privati/servizi/telepedaggio/tangenziale-napoli-autostrada-a56) |
| Orari di metro e bus | feed GTFS di ANM (orari programmati di linee e fermate) | [Transitland – ANM](https://transit.land/feed-registry/operators/o-s-aziendanapoletanamobilit) |
| Scossa del 31 luglio 2026 | Md 4.7 alle 19:46, treni sospesi, blackout e reti telefoniche in difficoltà | [INGV – Osservatorio Vesuviano, bollettino del 4 agosto 2026](https://www.ov.ingv.it/index.php/monitoraggio-e-infrastrutture/bollettini-tutti/boll-sett-flegrei/anno-2026/1996-bollettino-flegrei-2026-08-04/file); treni e blackout: [Sky TG24](https://tg24.sky.it/cronaca/2026/07/31/terremoto-napoli-oggi) |
| Crociere nel porto di Napoli | circa 1,85 milioni di passeggeri nel 2025 | Cemar, via [Shipping Italy](https://www.shippingitaly.it/2026/01/19/cemar-nel-2025-quasi-148-milioni-di-crocieristi-nei-porti-italiani-4/) |
| Cantieri e chiusure | chiusure notturne in Tangenziale, novembre 2026 | Napolike, 14 novembre 2026 |

## Sensori IoT già in strada
I sensori servono a Jammo in due modi: come **dati** (quante auto passano, dove si forma la coda) e come **leve** (i tempi dei semafori e i messaggi sui pannelli, un canale in più per chi non ha l’app).

| Infrastruttura | Cosa c’è | Uso in Jammo | Fonte |
|---|---|---|---|
| Tangenziale di Napoli, prima smart road certificata dal MIT (giugno 2026) | 217 telecamere intelligenti, 15 portali di rilevamento, 8 centraline meteo, 40 antenne V2X; dati sulla piattaforma C-ITS di Movyon; circa 3,5 milioni di dati di transito al giorno | auto per rampa e per fascia oraria, velocità, pioggia e stato dell’asfalto | [Euronews](https://it.euronews.com/next/2026/06/11/tangenziale-di-napoli-e-la-prima-smart-road-ditalia-cosi-cambia-la-mobilita-del-futuro), [ItaliaOggi](https://www.italiaoggi.it/economia-e-politica/economia-e-finanza/e-a-napoli-la-prima-smart-road-ditalia-mpxqxpd5), [AGI](https://www.agi.it/economia/news/2025-05-22/dynamic-speed-limit-tangenziale-napoli-mobilita-intelligente-31511054/) |
| Comune di Napoli, sala operativa centrale | semafori intelligenti con telecamere (prime prove a Fuorigrotta e Agnano) e pannelli a messaggio variabile | code agli incroci; tempi dei semafori (per esempio un verde più lungo all’uscita di un concerto); messaggi sui pannelli | [Napolike](https://www.napolike.com/semafori-intelligenti-a-napoli-con-le-telecamere-a-fuorigrotta-e-agnano-come-funzionano), [Fanpage](https://www.fanpage.it/napoli/cosa-sono-i-pannelli-luminosi-installati-nelle-strade-di-napoli-in-questi-giorni/) |

## Dati simulati (servono accordi)
| Dato | Perché è simulato | Da chi arriverebbe |
|---|---|---|
| Auto per rampa e per fascia oraria | i sensori esistono, ma i dati non sono pubblici | sensori IoT della Tangenziale (piattaforma C-ITS) |
| Code agli incroci | i dati non sono pubblici | semafori intelligenti del Comune |
| Presenze per zona | non pubblico | rete mobile (Fastweb, Vodafone) |
| Ingressi in stazione | non pubblico | tornelli ANM, EAV, Trenitalia |
| Prenotazioni delle escursioni | non pubblico | compagnie crocieristiche e turistiche |
| Orari e destinazioni degli utenti | l’app non esiste ancora | app Jammo, senza nome |

Non servono dati in tempo reale: le stime si fanno in anticipo, sul traffico tipico e sui piani confermati. Quando arrivano gli accordi, i sensori IoT servono a correggere le stime durante la giornata.