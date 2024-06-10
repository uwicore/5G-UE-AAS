#Imports
from AAS5GUEsubmodels import *       #Here we have the created structure for the AAS


#We need to import the AASs
from UE_5G_AAS import listOfUeAASs


#For make some prints to check it is imported correctly 
print(listOfUeAASs[0].id_short)
print(listOfUeAASs[0].location.xPosition.id_short)

print(listOfUeAASs[0].ueAttachAndConnectionStatus.pduSessionList.pduSessions[0].qosFlowList.qosFlows[0])

#Changing some values in 5G_UE_AAS to understand how it works
listOfUeAASs[0].qosMonitoring.parametersPertainingConnections.pduSessionList.pduSessions[0].qosFlowList.qosFlows[0].serviceBitRate.value=85
listOfUeAASs[0].ue5GIdentification.permanentEquipmentIdentifier.value=2976
listOfUeAASs[0].ueAttachAndConnectionStatus.pduSessionList.pduSessions[0].linkDirection.value="Uplink"




'''
If there is more than one 5G UE AAS you can use the list of Ues like these examples:
listOfUeAASs[1].qosMonitoring.updateTime.value=18
print(listOfUeAASs[1].qosMonitoring.generalKeyPerformanceIndicators.bler.value)
'''
