from spyne import Application
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument

from .Services import ElectricCarServices

app: Application = Application([ElectricCarServices],
                          tns='spyne.examples.hello',
                          in_protocol=HttpRpc(validator='soft'),
                          out_protocol=JsonDocument()
)