from mycroft import MycroftSkill, intent_file_handler


class InternalNetworkForProductionMachines(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('machines.production.for.network.internal.intent')
    def handle_machines_production_for_network_internal(self, message):
        self.speak_dialog('machines.production.for.network.internal')


def create_skill():
    return InternalNetworkForProductionMachines()

