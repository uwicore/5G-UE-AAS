from aas import model
from aas.adapter import aasx
import aas
from aas.model import AssetKind, Constraint, ModelingKind, Reference, Submodel, SubmodelElement, SubmodelElementCollectionOrdered, SubmodelElementCollectionUnordered, Property, Identifier,Operation, SubmodelElementCollection, MultiLanguageProperty, Asset, AssetAdministrationShell, AASReference, Asset, Identifier, LangStringSet, Namespace, AdministrativeInformation, Security, Submodel, ConceptDictionary, View, AbstractObjectProvider  # Importa las clases necesarias
import abc
from typing import Optional, Set, Iterable, TYPE_CHECKING, List, Type
import math
from aas.model import base, datatypes
from aas.model.base import Constraint, LangStringSet, ModelingKind, Namespace, Reference
from aas.model.submodel import OperationVariable, SubmodelElement
if TYPE_CHECKING:
    from . import aas


class UE5G(Asset):
    def __init__(self, kind: AssetKind, identification: Identifier, id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, asset_identification_model: AASReference[Submodel] | None = None, bill_of_material: AASReference[Submodel] | None = None):
            super().__init__(kind, identification, id_short, category, description, parent, administration, asset_identification_model, bill_of_material)



class AASUE5G(AssetAdministrationShell):
    def __init__(self, asset_real,nameplate,identification_submodel,documentation,service,technicalData,ue5GIdentification,networkAccessRestrictions,ueAttachAndConnectionStatus,qos_monitoring, location, ue5GDatasheet, asset: AASReference[Asset], identification: Identifier, id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, security: Security | None = None, submodel: Set[AASReference[Submodel]] | None = None, concept_dictionary: Iterable[ConceptDictionary] = ..., view: Iterable[View] = ..., derived_from: AASReference[AssetAdministrationShell] | None = None):
       self.asset_real=asset_real
       self.nameplate=nameplate
       self.identification_submodel=identification_submodel
       self.documentation=documentation
       self.service=service
       self.technicalData=technicalData
       self.ue5GIdentification=ue5GIdentification
       self.networkAccessRestrictions=networkAccessRestrictions
       self.ueAttachAndConnectionStatus=ueAttachAndConnectionStatus
       self.qosMonitoring=qos_monitoring
       self.location=location
       self.ue5GDatasheet=ue5GDatasheet
       super().__init__(asset, identification, id_short, category, description, parent, administration, security, submodel, concept_dictionary, view, derived_from)
    
#UeAttachAndConnectionStatus Submodel


class NewConnectionRequest(Operation):
    def __init__(self, id_short: str, input_variable: List[OperationVariable] | None = None, output_variable: List[OperationVariable] | None = None, in_output_variable: List[OperationVariable] | None = None, category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.input_variable=input_variable
        self.output_variable=output_variable
        self.in_output_variable=in_output_variable
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind=kind


class ConnectionModificationRequest(Operation):
    def __init__(self, id_short: str, input_variable: List[OperationVariable] | None = None, output_variable: List[OperationVariable] | None = None, in_output_variable: List[OperationVariable] | None = None, category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.input_variable=input_variable
        self.output_variable=output_variable
        self.in_output_variable=in_output_variable
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind=kind


class QosParameters(SubmodelElementCollectionUnordered):


    def __init__(self, qos_identifier, arp, rqa, notification_control, gfbr_ul, gfbr_dl, mfbr_ul, mfbr_dl, max_packet_loss_rate, aggregate_bit_rates, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        
        self.qosIdentifier = qos_identifier
        self.arp = arp
        self.rqa = rqa
        self.notificationControl = notification_control
        self.gfbrul = gfbr_ul
        self.gfbrdl = gfbr_dl
        self.mfbrul = mfbr_ul
        self.mfbrdl = mfbr_dl
        self.maximumPacketLossRate = max_packet_loss_rate
        self.aggregateBitRates = aggregate_bit_rates
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
      

class QosCharacteristics(SubmodelElementCollectionUnordered):
    def __init__(self, resource_type, priority_level, packet_delay_budget, packet_error_rate, averaging_window, max_data_burst_volume, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.resourceType = resource_type
        self.priorityLevel = priority_level
        self.packetDelayBudget = packet_delay_budget
        self.packetErrorRate = packet_error_rate
        self.averagingWindow = averaging_window
        self.maximumDataBurstVolume = max_data_burst_volume
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
              

class QosProfile(SubmodelElementCollectionUnordered):
    def __init__(self, qos_parameters, qos_characteristics, alternativeQosProfile, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.qosParameters = qos_parameters
        self.qosCharacteristics = qos_characteristics
        self.alternativeQosProfile=alternativeQosProfile
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class AlternativeQosProfile(SubmodelElementCollectionUnordered):
    def __init__(self, qos_parameters, qos_characteristics, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.qosParameters = qos_parameters
        self.qosCharacteristics = qos_characteristics
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class AlternativeQosProfiles(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.alternativeQosProfiles = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_alternative_qos_profile(self, alternative_qos_profile):
        self.alternativeQosProfiles.append(alternative_qos_profile)
    
    def remove_alternative_qos_profile(self, alternative_qos_profile):
        if alternative_qos_profile in self.alternativeQosProfiles:
            self.alternativeQosProfiles.remove(alternative_qos_profile)
            
        else:
            print("AlternativeQosProfile did not find in the list")


class RRMParameters(SubmodelElementCollectionUnordered):
    def __init__(self, mcstable, cqitable, target_bler, scheduling_type, scheduling_policy, harq_max_num_retransmissions, k_number, power_control_pmax, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.mcsTable = mcstable
        self.cqiTable = cqitable
        self.targetBLER = target_bler
        self.schedulingType = scheduling_type
        self.schedulingPolicy = scheduling_policy
        self.harqMaximumNumberOfRetransmissions = harq_max_num_retransmissions
        self.kNumber_ul = k_number
        self.powerControlPmax = power_control_pmax
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             


class QosFlowStatus(SubmodelElementCollectionUnordered):                      
    def __init__(self, qfi, qos_profileRequested, qos_profileGuaranteed, rrm_parameters, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.qfi = qfi              
        self.qosProfileRequested = qos_profileRequested
        self.qosProfileGuaranteed = qos_profileGuaranteed
        self.rrmParameters = rrm_parameters
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class QosFlowStatusList(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.qosFlows = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_qos_flow(self, qos_flow):
        self.qosFlows.append(qos_flow)

    def remove_qos_flow(self, qos_flow):
        if qos_flow in self.qosFlows:
            self.qosFlows.remove(qos_flow)
        else:
            print("QosFlow did not find in the list")


class PDUSessionStatus(SubmodelElementCollectionUnordered):
    def __init__(self,IPAddress,dnn, qos_flow_list, linkDirection, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.ipAddress=IPAddress 
        self.dnn=dnn
        self.linkDirection=linkDirection
        self.qosFlowList = qos_flow_list
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class PDUSessionStatusList(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.pduSessions = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_pdu_session(self, pdu_session):
        self.pduSessions.append(pdu_session)


    def remove_pdu_session(self, pdu_session):
        if pdu_session in self.pduSessions:
            self.pduSessions.remove(pdu_session)

        else:
            print("PDU session did not find in the list")


class UeAttachAndConnectionStatus(Submodel):
    def __init__(self,UeAttached, RRC_state,pdu_session_list, newConnectionRequest, connectionModificationRequest, qoSRequest, identification: base.Identifier,
                 submodel_element: Iterable[SubmodelElement] = (),
                 id_short: str = "",
                 category: Optional[str] = None,
                 description: Optional[base.LangStringSet] = None,
                 parent: Optional[base.Namespace] = None,
                 administration: Optional[base.AdministrativeInformation] = None,
                 semantic_id: Optional[base.Reference] = None,
                 qualifier: Optional[Set[base.Constraint]] = None,
                 kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.pduSessionList = pdu_session_list
        self.ueAttached= UeAttached
        self.rrcState= RRC_state
        self.newConnectionRequest=newConnectionRequest
        self.connectionModificationRequest=connectionModificationRequest
        self.qoSRequest=qoSRequest
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind


#NetworkAccessRestrictions Submodel

class ListOfCellGlobalIdentifier(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.cgis = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_cgi(self, cgi):
        self.cgis.append(cgi)

    def remove_cgi(self, cgi):
        if cgi in self.cgis:
            self.cgis.remove(cgi)
            
        else:
            print("CGI did not find in the list")



class ListOfPermissibleSlices(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.snssais = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_snssai(self, snssai):
        self.snssais.append(snssai)

    def remove_snssai(self, snssai):
        if snssai in self.snssais:
            self.snssais.remove(snssai)
            
        else:
            print("SNSSAI did not find in the list")

class NetworkAccessRestrictions(Submodel):
    def __init__(self,list_of_cgis, list_of_permissible_slices, identification: base.Identifier,
                 submodel_element: Iterable[SubmodelElement] = (),
                 id_short: str = "",
                 category: Optional[str] = None,
                 description: Optional[base.LangStringSet] = None,
                 parent: Optional[base.Namespace] = None,
                 administration: Optional[base.AdministrativeInformation] = None,
                 semantic_id: Optional[base.Reference] = None,
                 qualifier: Optional[Set[base.Constraint]] = None,
                 kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.listOfCellGlobalIdentifier = list_of_cgis
        self.listOfPermissibleSlices = list_of_permissible_slices
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
        
#QosMonitoring Submodel
class GeneralKeyPerformanceIndicators(SubmodelElementCollectionUnordered):
    def __init__(self, dropped_connections, traffic_volume_for_each_5qi_and_alternative_qos_profiles,handover_success_rate, sinr, data_throughput, bler, per, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.droppedConnections = dropped_connections
        self.trafficVolumeForEach5QIAndAlternativeQosProfiles = traffic_volume_for_each_5qi_and_alternative_qos_profiles
        self.handoverSuccessRate = handover_success_rate
        self.sinr = sinr
        self.dataThroughput = data_throughput
        self.bler = bler
        self.per = per
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class SignalLevel(SubmodelElementCollectionUnordered):
    def __init__(self, rssi, rsrp, rsrq, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.rssi = rssi
        self.rsrp = rsrp
        self.rsrq=rsrq
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class QosFlowMonitoring(SubmodelElementCollectionUnordered):                      
    def __init__(self, qfi, commservavai,commservrel, e2elm, e2elavg,survivaltime,servicebitrate,per,bler,updatetime,data_throughput, cause5gsm, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.qfi = qfi              
        self.communicationServiceAvailabilty=commservavai
        self.communicationServiceReliability=commservrel
        self.endToEndLatencyMaximum=e2elm
        self.endToEndLatencyAVG=e2elavg
        self.survivalTime=survivaltime
        self.serviceBitRate=servicebitrate
        self.packetErrorRatio=per
        self.bler=bler
        self.updateTime=updatetime
        self.dataThroughput=data_throughput
        self.cause5GSM=cause5gsm
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class QosFlowMonitoringList(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.qosFlows = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_qos_flow(self, qos_flow):
        self.qosFlows.append(qos_flow)

    def remove_qos_flow(self, qos_flow):
        if qos_flow in self.qosFlows:
            self.qosFlows.remove(qos_flow)
            
        else:
            print("QosFlow did not find in the list")

class PDUSessionMonitoring(SubmodelElementCollectionUnordered):
    def __init__(self,IPAddress,qos_flow_list, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.ipAddress=IPAddress 
        self.qosFlowList = qos_flow_list
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class PDUSessionMonitoringList(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.pduSessions = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_pdu_session(self, pdu_session):
        self.pduSessions.append(pdu_session)

    def remove_pdu_session(self, pdu_session):
        if pdu_session in self.pduSessions:
            self.pduSessions.remove(pdu_session)
            
        else:
            print("PDU session did not find in the list")


class ParametersPertainingConnections(SubmodelElementCollectionUnordered):
    def __init__(self, pdu_session_list, id_short: str,
                 value: Iterable[SubmodelElement] = (), category: Optional[str] = None, description: Optional[base.LangStringSet] = None, parent: Optional[base.Namespace] = None,
                 semantic_id: Optional[base.Reference] = None, qualifier: Optional[Set[base.Constraint]] = None, kind: base.ModelingKind = base.ModelingKind.INSTANCE):
        self.pduSessionList = pdu_session_list
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             


class QosQuery(Operation):
    def __init__(self, id_short: str, input_variable: List[OperationVariable] | None = None, output_variable: List[OperationVariable] | None = None, in_output_variable: List[OperationVariable] | None = None, category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.input_variable=input_variable
        self.output_variable=output_variable
        self.in_output_variable=in_output_variable
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind=kind
            
    #Functions in operations will developed later
    def query(self, qos_parameters, timespan):
        # Logic of the operation
        # result of the query
        result = None  #This will change
        return result



class EventNotificationAction(Operation):
    def __init__(self, id_short: str, input_variable: List[OperationVariable] | None = None, output_variable: List[OperationVariable] | None = None, in_output_variable: List[OperationVariable] | None = None, category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.input_variable=input_variable
        self.output_variable=output_variable
        self.in_output_variable=in_output_variable
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind=kind
        


class ListOfMonitoringSubscriptions(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.subscriptions = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_subscription(self, subscription):                                           
        self.subscriptions.append(subscription)

    def remove_subscription(self, subscription):
        if subscription in self.subscriptions:
            self.subscriptions.remove(subscription)

        else:
            print("Subscription did not find in the list")


class QosMonitoring(Submodel):
        def __init__(self, general_kpis, signal_level, parameters_pertaining_connections, qos_query, subscriptionRequest,subscriptionManagement, listOfMonitoringSubscriptions, listOfNWSubscriptions, updateTime, identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
            self.generalKeyPerformanceIndicators = general_kpis
            self.signalLevel = signal_level
            self.parametersPertainingConnections = parameters_pertaining_connections
            self.qosQuery=qos_query
            self.subscriptionRequest=subscriptionRequest
            self.subscriptionManagement=subscriptionManagement
            self.listOfSubscriptions=listOfMonitoringSubscriptions
            self.listOfNWSubscriptions=listOfNWSubscriptions
            self.updateTime=updateTime
            self.parent=parent
            self.identification=identification
            self.submodel_element=submodel_element
            self.id_short=id_short
            self.category=category
            self.description=description
            self.administration=administration
            self.semantic_id=semantic_id
            self.qualifier=qualifier
            self._kind= kind
            

        
#Location Submodel    

class ListOfLocalizationSubscriptions(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.subscriptions = []
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

    def add_subscription(self, subscription):                                           
        self.subscriptions.append(subscription)
 
    def remove_subscription(self, subscription):
        if subscription in self.subscriptions:
            self.subscriptions.remove(subscription)
            
        else:
            print("Subscription did not find in the list")

class LocationUE(Submodel):
    def __init__(self, xPosition, yPosition,zPosition,speed, aceleration, lcs_qos_class, accuracy, response_time, list_of_subscriptions, listOfNWSubscriptions, subcriptionRequest, subcriptionManagement,  identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.zPosition = zPosition
        self.speed=speed
        self.aceleration=aceleration
        self.lcsQosClass = lcs_qos_class
        self.accuracy = accuracy
        self.responseTime = response_time
        self.listOfSubscriptions= list_of_subscriptions
        self.listOfNWSubscriptions=listOfNWSubscriptions
        self.subcriptionRequest=subcriptionRequest
        self.subcriptionManagement=subcriptionManagement
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
        
#Nameplate Submodel
class PhysicalAddress(SubmodelElementCollectionUnordered):
    def __init__(self, country_code, street, postal_code, city, state_county, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.countryCode=country_code
        self.street=street
        self.postalCode=postal_code
        self.city=city
        self.stateCounty=state_county
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class Nameplate(Submodel):
    def __init__(self,manufacturer_name,manufacturer_typ_name,physical_address, typ_class, serialno, chargeid,countryoforigin,yearofconstruction, identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., 
                 id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.manufacturerName=manufacturer_name
        self.manufacturerTypName=manufacturer_typ_name
        self.physicalAddress=physical_address
        self.typClass=typ_class
        self.serialNo=serialno
        self.chargeId=chargeid
        self.countryOfOrigin= countryoforigin
        self.yearOfConstruction= yearofconstruction
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
        


#Identification Submodel
class ContactInfo(SubmodelElementCollectionUnordered):
    def __init__(self,name,role,physical_address,email,url,phone, fax, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.name=name
        self.role=role
        self.physicalAddress= physical_address
        self.email=email
        self.url=url
        self.phone=phone
        self.fax=fax
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             


class Identification(Submodel):
    def __init__(self, manufacturer_name, manufacturer_id, manufacturer_idprovider, manufacturer_typid, manufacturer_typname, manufacturer_typdesc, suppliername, supplierid,supplierid_provider, supplier_typid, supplier_typname, supplier_typdesc, typclass,classystem,
                 seckeytyp, asset_id, instance_id, chargeid,seckeyinst, manufacturing_date, device_rev, software_rev, hardware_rev, ContactInfo, url, identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.manufacturerName=manufacturer_name
        self.manufacturerId=manufacturer_id
        self.manufacturerIdProvider=manufacturer_idprovider
        self.manufacturerTypId= manufacturer_typid
        self.manufacturerTypName= manufacturer_typname
        self.manufacturerTypDescription=manufacturer_typdesc
        self.supplierName=suppliername
        self.supplierId=supplierid
        self.supplierIdProvider=supplierid_provider
        self.supplierTypId=supplier_typid
        self.supplierTypName=supplier_typname
        self.supplierTypDescription=supplier_typdesc
        self.typClass=supplier_typdesc
        self.classificationSystem=classystem
        self.secondaryKeyTyp=seckeytyp
        self.assetId=asset_id
        self.instanceId=instance_id
        self.chargeId=chargeid
        self.secondaryKeyInstance=seckeyinst
        self.manufacturingDate=manufacturing_date
        self.deviceRevision=device_rev
        self.softwareRevision=software_rev
        self.hardwareRevision=hardware_rev
        self.contactInfo=ContactInfo
        self.url=url
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
        
                
#Documentation Submodel

class Documentation(Submodel):
    def __init__(self, identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
        




#Service Submodel
class Service(Submodel):
    def __init__(self, contact_info,identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.contactInfo=contact_info
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
        

#TechnicalData Submodel
        
class GeneralInformation(SubmodelElementCollectionUnordered):
    def __init__(self, manufacturer_name, manufacturer_productdesignations,manufacturer_partnumber,manufacturer_ordercode, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.manufacturerName= manufacturer_name
        self.manufacturerProductDesignations=manufacturer_productdesignations
        self.manufacturerpartNumber=manufacturer_partnumber
        self.manufacturerOrdeCcode=manufacturer_ordercode
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class ProductClassificationItem(SubmodelElementCollectionUnordered):
    def __init__(self,prodclassys,classifsysvers,productclassid, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.productClassificationSystem= prodclassys
        self.classificationSystemVersion=classifsysvers
        self.productClassId=productclassid
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class ProductClassifications(SubmodelElementCollectionUnordered):
    def __init__(self, prodclassitem, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.productClassificationItem=prodclassitem
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             



class TechnicalProperties(SubmodelElementCollectionUnordered):
    def __init__(self, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind             

class FurtherInformation(SubmodelElementCollectionUnordered):
    def __init__(self, txt_statement,validate, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.textStatement=txt_statement
        self.validDate=validate
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             


class TechnicalData(Submodel):
    def __init__(self,geninfo,prodclass,techprop,furtherinfo, identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.generalInformation=geninfo
        self.productClassifications=prodclass
        self.technicalProperties=techprop
        self.furtherInformation=furtherinfo
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
                


#UE5GDataSheet
class UEChannelBandwidth(SubmodelElementCollectionUnordered):
    def __init__(self, maxtxbw, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.maximumTransmissionBandwidth= maxtxbw
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             


class OutputPowerDynamics(SubmodelElementCollectionUnordered):
    def __init__(self, minoutpower,txoffpower,id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.minimumOutputPower=minoutpower
        self.transmitOFFPower=txoffpower
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class TransmitterCharacteristics(SubmodelElementCollectionUnordered):
    def __init__(self,uemaxoutpower,outpowerdynamic, txsignalquality, outrfspecemissions, num_antenas, num_layers, maximumDataUplink, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.ueMaximumOutputPower= uemaxoutpower
        self.outputPowerDynamics= outpowerdynamic
        self.transmitSignalQuality= txsignalquality
        self.outputRFSpectrumEmissions= outrfspecemissions
        self.numberOfAntennas= num_antenas
        self.numberOfLayers=num_layers
        self.maximumDataUplink=maximumDataUplink
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class ReceiverCharacteristics(SubmodelElementCollectionUnordered):
    def __init__(self, refsenspowerlvl,maxinlvl,adjchannelselect,num_antenas, num_layers, maximumDataDownlink, id_short: str, value: Iterable[SubmodelElement] = ..., category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.referenceSensitivityPowerLevel=refsenspowerlvl
        self.maximumInputLevel=maxinlvl
        self.adjacentChannelSelectivity=adjchannelselect
        self.numberOfAntennas= num_antenas
        self.numberOfLayers=num_layers
        self.maximumDataDownlink=maximumDataDownlink
        self.parent=parent
        self._id_short=id_short
        self.id_short=id_short
        self.value=value
        self.category=category
        self.description=description
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
             

class UE5GDataSheet(Submodel):
    def __init__(self,opbands,ue_channel_bw, duplex_mode, tx_characteristics, rx_characteristics, identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.operatingBands=opbands
        self.ueChannelBandwidth=ue_channel_bw
        self.duplexMode=duplex_mode
        self.transmitterCharacteristics= tx_characteristics
        self.receiverCharacteristics=rx_characteristics
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind


#Ue5GIdentification Submodel
class Ue5GIdentification(Submodel):
    def __init__(self, pei,gpsi,authcertificate,certificatestatus, ipAddress, macAddress, imsi,spn, pin, iccid, identification: Identifier, submodel_element: Iterable[SubmodelElement] = ..., id_short: str = "", category: str | None = None, description: LangStringSet | None = None, parent: Namespace | None = None, administration: AdministrativeInformation | None = None, semantic_id: Reference | None = None, qualifier: Set[Constraint] | None = None, kind: ModelingKind = base.ModelingKind.INSTANCE):
        self.permanentEquipmentIdentifier=pei
        self.ueIdentityGPSI=gpsi
        self.authenticationCertificate=authcertificate
        self.certificateStatus=certificatestatus
        self.ipAddress=ipAddress
        self.macAddress=macAddress
        self.imsi=imsi
        self.spn=spn
        self.pin=pin
        self.iccid=iccid
        self.parent=parent
        self.identification=identification
        self.submodel_element=submodel_element
        self.id_short=id_short
        self.category=category
        self.description=description
        self.administration=administration
        self.semantic_id=semantic_id
        self.qualifier=qualifier
        self._kind= kind
        



