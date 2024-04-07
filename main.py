import dpkt
import socket
import pygeoip


gi = pygeoip.GeoIP('GeoLiteCity.dat') 

def main():
    f = open('proba.pcap', 'rb')
    pcap = dpkt.pcap.Reader(f) 
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
    '<Style id="yellowLineGreenPoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>7fff0000</color>' \
                '</LineStyle>' \
                '</Style>' 
    kmlfooter = '</Document>\n</kml>\n' 
    kmldoc=kmlheader+praviIp(pcap)+kmlfooter 
    print(kmldoc)

def praviIp(pcap):
    kmlPts = ''
    for (ts, buf) in pcap: 
        try:
            eth = dpkt.ethernet.Ethernet(buf) 
            ip = eth.data 
            izvor = socket.inet_ntoa(ip.src) #IZ 10101010 10101010 10101010 10101010 U 192.168.8.1
            destinacija = socket.inet_ntoa(ip.dst) 
            KML = retKML(destinacija, izvor) #returnKML vraća kml fajl sa ip adresom izvora i destinacije
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts

def retKML(dstip, srcip):
    destinacija = gi.record_by_name(dstip) 
    izvor = gi.record_by_name('178.220.212.173') 

    try:
        destDuzina = destinacija['longitude']  
        destSirina = destinacija['latitude'] 
        izvDuzina = izvor['longitude']
        izvSirina = izvor['latitude']
        kml = (           #telo KML fajla u kom uzimamo podatke iz pcap-a
            '<Placemark>\n'
            '<name>%s</name>\n' 
            '<extrude>1</extrude>\n' #extends the line down to the ground.
            '<tessellate>1</tessellate>\n' #breaks the line up into smaller chunks
            '<styleUrl>#yellowLineGreenPoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        )%(dstip, destDuzina, destSirina, izvDuzina, izvSirina)
        return kml
    except:
        return ''

main()