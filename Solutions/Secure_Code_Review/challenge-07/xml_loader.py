from defusedxml import ElementTree as ET


def load(xml_bytes):
    return ET.fromstring(xml_bytes)
