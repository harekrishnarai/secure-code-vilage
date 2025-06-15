import xml.etree.ElementTree as ET


def load(xml_bytes):
    return ET.fromstring(xml_bytes)
