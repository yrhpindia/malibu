# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import requests
import json
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name, is_request_type

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=11"
        # response = requests.get(url)
        # the_fact = response.text
        # speech=the_fact
        speech = " Welcome to Malibu, How can i help you ?"
        return (
            handler_input.response_builder
                .speak(speech)
                .ask(" You can ask me to perform any of the commnads given in your menu.")
                .ask(" You can place order by saying Alexa, Add one quantity of ten.")
                .response
        )

class setwelcomeIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("setwelcomeIntent")(handler_input))
    def handle(self, handler_input):
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=101"
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        reprompt = " now You can give order."
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = " Try again"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("  Sorry, I can't understand what You said.")
                .ask(" If there is a problem call helper near You.")
                .response
        )

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for skill session end."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")
        print("Session ended with reason: {}".format(
            handler_input.request_envelope))
        return handler_input.response_builder.response

class additemIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("additemIntent")(handler_input))
    def handle(self, handler_input):
        theid=None
        quantity=None
        # type: (HandlerInput) -> Response
        theid = handler_input.request_envelope.request.intent.slots["itemid"].value
        quantity = handler_input.request_envelope.request.intent.slots["quantity"].value
        user_id = handler_input.request_envelope.context.system.device.device_id
        did = "01"
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=1&itemid="+theid+"&quantity="+quantity
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        # speech = " devide id  "+user_id
        reprompt=" To remove product , you can say alexa remove "+quantity+" quantity of "+theid
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class removeitemIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("removeitemIntent")(handler_input))
    def handle(self, handler_input):
        theid=None
        quantity=None
        # type: (HandlerInput) -> Response
        theid = handler_input.request_envelope.request.intent.slots["itemid"].value
        quantity = handler_input.request_envelope.request.intent.slots["quantity"].value
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=2&itemid="+theid+"&quantity="+quantity
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        reprompt = " Confirming your order is compulsory to get it prepared."
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class showorderIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("showorderIntent")(handler_input))
    def handle(self, handler_input):
        # const { deviceId } = requestEnvelope.context.System.device;
        
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=3"
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact;
        reprompt = " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class resetorderIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("resetorderIntent")(handler_input))
    def handle(self, handler_input):
        # theid=None
        # # type: (HandlerInput) -> Response
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=4"
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        reprompt = " here is a tip , confirmed products can not be reseted , so check list before you confirm."
        # speech = "in reset order"
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class completeorderIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("completeorderIntent")(handler_input))
    def handle(self, handler_input):
        attr = handler_input.attributes_manager.session_attributes
        attr["flag"] = 1
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=51"
        # deviceId = this.event.context.System.device.deviceId
        response = requests.get(url)
        the_fact = response.text
        # speech = the_fact+"Your device id is "+deviceId
        speech = the_fact
        reprompt = " you can say yes ,if list is okay. or  else say no  and remove or add something."
        # speech = " in complete order   "+"con+firm ?"
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class YesIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("AMAZON.YesIntent")(handler_input))
    def handle(self, handler_input):
        attr = handler_input.attributes_manager.session_attributes
        if attr.get("flag") == 1:
            url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=5"
            response = requests.get(url)
            the_fact = response.text
            speech = the_fact
            reprompt= " "
        elif attr.get("flag") == 2:
            url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=8"
            response = requests.get(url)
            the_fact = response.text
            speech = the_fact
            reprompt= " "
        else:
            speech=" "
            attr["flag"] = 0
            reprompt= " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_should_end_session(True)
        return handler_input.response_builder.response

class NoIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("AMAZON.NoIntent")(handler_input))
    def handle(self, handler_input):
        attr = handler_input.attributes_manager.session_attributes
        if attr.get("flag") == 1:
            speech = " order not confirmed. Please, Add or remove items and reconfirm Order "
            reprompt= " here is a tip , to check products of your orderlist you can say like show my order."
        elif attr.get("flag") == 2:
            speech = " your bill is not generated , make sure you are done eating before you ask for bill."
            reprompt= " "
        else:
            speech=" "
            attr["flag"] = 0
            reprompt = "  "
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_should_end_session(True)
        return handler_input.response_builder.response

class orderstatusIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("orderstatusIntent")(handler_input))
    def handle(self, handler_input):
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=6"
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        reprompt= " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class itemstatusIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("itemstatusIntent")(handler_input))
    def handle(self, handler_input):
        theid = handler_input.request_envelope.request.intent.slots["itemid"].value
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=7&itemid="+theid
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        reprompt= " "
        # speech = " in complete order   "+"confirm ?"
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class billorderIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("billorderIntent")(handler_input))
    def handle(self, handler_input):
        attr = handler_input.attributes_manager.session_attributes
        attr["flag"] = 2
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=81"
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        # speech = " in bill order  "
        reprompt= " here is a tip, before asking your bill check if all your order is served to your table."
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class productidIntentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("productidIntent")(handler_input))
    def handle(self, handler_input):
        thename = handler_input.request_envelope.request.intent.slots["itemname"].value
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=10&productname="+thename
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        reprompt = " "
        # speech = " in bill order  "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class idnameHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("idname")(handler_input))
    def handle(self, handler_input):
        theid=None
        quantity=None
        # type: (HandlerInput) -> Response
        theid = handler_input.request_envelope.request.intent.slots["itemid"].value
        url = "https://www.yrhp.in/T-Talkiee/placeorder-verify.php?status=9&itemid="+theid
        response = requests.get(url)
        the_fact = response.text
        speech = the_fact
        reprompt = " Confirming your order is compulsory to get it prepared."
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class howtoaddintentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("howtoaddintent")(handler_input))
    def handle(self, handler_input):
        speech = "  For example , To Add two Manchurian in your orderlist You have to say like  Alexa , Add two quantity of oneeighty. "
        reprompt = " now You can give order."
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class howtoremoveintentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("howtoremoveintent")(handler_input))
    def handle(self, handler_input):
        speech = "  For example , To remove one  Manchurian in your orderlist You have to say like  Alexa , remove one quantity of one eighty. "
        reprompt = " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class howtoshowintentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("howtoshowintent")(handler_input))
    def handle(self, handler_input):
        speech = "  For example,  To show your orderlist You have to say like  Alexa , show my orderlist. "
        reprompt = " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class howtoresetintentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("howtoresetintent")(handler_input))
    def handle(self, handler_input):
        speech = "  reset means your unconfirm order will reset , You have to say like  Alexa , reset my orderlist , or clear my orderlist. "
        reprompt = " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class howtoconfirmHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("howtoconfirm")(handler_input))
    def handle(self, handler_input):
        speech = "  after confirming order , your order will be pass to chef , please make sure your orderlist is proper as product can't be removed , to confirm your order , You have to say like  Alexa , confirm my order. "
        reprompt = " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class howtoallstatusintentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("howtoallstatusintent")(handler_input))
    def handle(self, handler_input):
        speech = " To see all item status you can say Alexa , show my order status "
        reprompt = " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class howtoitemstatusintentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("howtoitemstatusintent")(handler_input))
    def handle(self, handler_input):
        speech = " To see particular item status you can say Alexa , check status of six. "
        reprompt = " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class howtobillintentHandler(AbstractRequestHandler):
    """Handler for get number fact intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or 
            is_intent_name("howtobillintent")(handler_input))
    def handle(self, handler_input):
        speech = " To make sure after asking for bill you can not add item , you can say Alexa , give my bill or bill please. "
        reprompt = " "
        handler_input.response_builder.speak(speech).ask(reprompt)
        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


# class SessionEndedRequestHandler(AbstractRequestHandler):
#     """Handler for Session End."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response

#         # Any cleanup logic goes here.

#         return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(setwelcomeIntentHandler())
sb.add_request_handler(additemIntentHandler())
sb.add_request_handler(removeitemIntentHandler())
sb.add_request_handler(resetorderIntentHandler())
sb.add_request_handler(showorderIntentHandler())
sb.add_request_handler(completeorderIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(orderstatusIntentHandler())
sb.add_request_handler(itemstatusIntentHandler())
sb.add_request_handler(billorderIntentHandler())
sb.add_request_handler(productidIntentHandler())
sb.add_request_handler(idnameHandler())
sb.add_request_handler(howtoaddintentHandler())
sb.add_request_handler(howtoremoveintentHandler())
sb.add_request_handler(howtoshowintentHandler())
sb.add_request_handler(howtoresetintentHandler())
sb.add_request_handler(howtoconfirmHandler())
sb.add_request_handler(howtoallstatusintentHandler())
sb.add_request_handler(howtoitemstatusintentHandler())
sb.add_request_handler(howtobillintentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()