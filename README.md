# Python-Packet-Sniffing
Created network analysis tool with Python &amp; Wireshark. Transformed data into KML for geo-analysis. Integrated GeoLiteCity for IP mapping. Developed Google Maps interface for user-friendly IP interaction.

//SERBIAN// ENGLISH BELLOW

1. Prvo što moramo uraditi je kreirati naše ulazne podatke u Wireshark-u tako što ćemo hvatati pakete i njih sačuvati u .pcap formatu. Pcap fajl će se sastojati od celokupnog mrežnog saobraćaja koji ulazi i izlazi iz našeg uređaja tokom perioda kada je funkcija hvatanja paketa aktivirana.

2. Pre svega neophodno je ubaciti sačuvani .pcap fajl iz Wireshark-a na istu lokaciju na računaru gde se nalazi i Python kod koji koristimo za ovaj projekat. Kroz main() metodu, koja nam je i glavna metoda u Python-u, otvaramo .pcap fajl sa snimljenim podacima uhvaćenog mrežnog saobraćaja, čitamo .pcap fajl preko dpkt biblioteke i pretvaramo ih u KML format, koji je izlazna datoteka koju koristimo za vizuelni prikaz u Google mapi/Google Earth.

Nakon pokretanja programa dobijamo kompletan KML fajl odštampan na terminalu. Ostaje samo da kopiramo ove podatke u datoteku i da joj damo ekstenziju .kml.

3. Nakon kreiranja našeg .kml fajla kroz Python skriptu, preko Google My mape kreiramo novu mapu i importujemo novi layer. Importujemo naš .kml fajl sa našeg kompjutera, i nakon toga nam se prikazuje mrežni saobraćaj na mapi.


//ENGLISH//

1. First, we need to create our input data in Wireshark by capturing packets and saving them in .pcap format. The pcap file will consist of all network traffic entering and leaving our device during the period when the packet capture function is active.

2. First and foremost, it is necessary to place the saved .pcap file from Wireshark in the same location on the computer where the Python code is used for this project is located. Through the main() method, which serves as the primary method in Python, we open the .pcap file containing the captured network traffic data, read the .pcap file using the dpkt library, and convert it into KML format. The KML file serves as the output file used for visual representation in Google Maps/Google Earth.

After running the program, we receive the complete KML file printed on the terminal. All that remains is to copy this data into a text file and give it the .kml extension.

3. After creating our .kml file through the Python script, we use Google My Maps to create a new map and import a new layer. We import our .kml file from our computer, and then the network traffic is displayed on the map.
