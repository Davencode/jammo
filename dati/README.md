# Dati usati da Jammo

Il prototipo usa **dati reali** dove sono pubblici e **dati simulati** dove servirebbero accordi con aziende ed enti. Ogni parametro della simulazione è in `parametri.json`, con il tipo (reale, simulato o ipotesi) e la fonte.

## Dati reali
| Dato | Valore | Fonte |
|---|---|---|
| Traffico in Tangenziale | circa 270.000 transiti al giorno | Tangenziale di Napoli SpA, via [Telepass](https://www.telepass.com/it/privati/servizi/telepedaggio/tangenziale-napoli-autostrada-a56) |
| Sensori sulla Tangenziale (smart road) | 217 telecamere, 40 antenne, circa 3,5 milioni di dati di transito al giorno | [ItaliaOggi](https://www.italiaoggi.it/economia-e-politica/economia-e-finanza/e-a-napoli-la-prima-smart-road-ditalia-mpxqxpd5), [AGI](https://www.agi.it/economia/news/2025-05-22/dynamic-speed-limit-tangenziale-napoli-mobilita-intelligente-31511054/) |
| Orari di metro e bus | Linea 1 ogni 8 minuti circa; feed GTFS di ANM | [Transitland – ANM](https://transit.land/feed-registry/operators/o-s-aziendanapoletanamobilit) |
| Scossa del 31 luglio 2026 | Md 4.7 alle 19:46, treni sospesi, blackout e reti telefoniche in difficoltà | INGV, via [Geopop](https://www.geopop.it/campi-flegrei-245-terremoti-in-una-settimana-e-700-sfollati-il-bollettino-ingv-dopo-la-scossa-di-md-4-7/), [Open](https://www.open.online/2026/07/31/terremoto-a-napoli-scossa-di-magnitudo-4-7-ai-campi-flegrei-il-video/) |
| Crociere nel porto di Napoli | circa 1,85 milioni di passeggeri nel 2025 | Cemar, via [Shipping Italy](https://www.shippingitaly.it/2026/01/19/cemar-nel-2025-quasi-148-milioni-di-crocieristi-nei-porti-italiani-4/) |
| Cantieri e chiusure | chiusure notturne in Tangenziale, novembre 2026 | Napolike, 14 novembre 2026 |

## Dati simulati (servono accordi)
| Dato | Perché è simulato | Da chi arriverebbe |
|---|---|---|
| Auto per rampa e per fascia oraria | non pubblico | sensori della Tangenziale |
| Presenze per zona | non pubblico | rete mobile (Fastweb, Vodafone) |
| Ingressi in stazione | non pubblico | tornelli ANM, EAV, Trenitalia |
| Prenotazioni delle escursioni | non pubblico | compagnie crocieristiche e turistiche |
| Orari e destinazioni degli utenti | l’app non esiste ancora | app Jammo, senza nome |

Non servono dati in tempo reale: le stime si fanno in anticipo, sul traffico tipico e sui piani confermati.
