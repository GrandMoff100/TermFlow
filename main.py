from flowcharts import Elem, Flow, View

four = Elem('4')

four << '3' << '2' << '1' << '0'
four >> '5' >> '6' >> '7'

four << '3a' << '2a' << '1a' << '0a'
four >> '5a' >> '6a' >> '7a'


flow = Flow(four)
view = View(flow)
