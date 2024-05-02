import requests
import xml.etree.ElementTree as ET

# Define the SOAP request as an XML string
xml_request = """
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cwmp="http://www.openmobilealliance.org/xml/protocol/cwmp-2-2">
  <SOAP-ENV:Header/>
  <SOAP-ENV:Body>
    <cwmp:Inform>
      <DeviceId>
        <Manufacturer>Huawei Technologies Co., Ltd.</Manufacturer>
        <OUI>00:10:18</OUI>
        <ProductClass>HG532s</ProductClass>
        <SerialNumber>XYZABCDEFG12345678</SerialNumber>
      </DeviceId>
      <CurrentTime>2023-04-21T14:00:00Z</CurrentTime>
      <ParameterList>
        <ParameterKey>
          <Name>InternetGatewayDevice.ManagementServer.ParameterKey.1</Name>
          <Value>123456</Value>
        </ParameterKey>
        <ParameterKey>
          <Name>InternetGatewayDevice.ManagementServer.CommandKey.1</Name>
          <Value>reboot</Value>
        </ParameterKey>
      </ParameterList>
    </cwmp:Inform>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

# Parse the XML string into an ElementTree object
xml_root = ET.fromstring(xml_request)

# Send the SOAP request to the target device using the requests library
try:
    response = requests.post("http://10.0.2.15:7547/", headers={"Content-Type": "text/xml"}, data=ET.tostring(xml_root), timeout=10)
    print("Response headers:", response.headers)
    print("Response content:", response.content)
except requests.exceptions.RequestException as e:
    print("Request failed:", str(e))
