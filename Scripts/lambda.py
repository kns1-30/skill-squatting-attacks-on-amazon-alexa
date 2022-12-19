import json
# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging

import os
import boto3
from ask_sdk_core.skill_builder import SkillBuilder
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_dynamodb.adapter import DynamoDbAdapter

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# ddb_region = os.environ.get('us-east-1')
# ddb_table_name = os.environ.get('7908c576-9d87-46bd-af99-d6a431ee549c')

# ddb_resource = boto3.resource('dynamodb', region_name=ddb_region)
# dynamodb_adapter = DynamoDbAdapter(table_name=ddb_table_name, create_table=False, dynamodb_resource=ddb_resource)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):

        speak_output= "in launch";

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("")
                .response
        )


class RecordIntentHandler(AbstractRequestHandler):
    """Handler for record Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return  ask_utils.is_intent_name("record")(handler_input)

    def handle(self, handler_input):
    # type: (HandlerInput) -> Response

    # 3. Perform DynamoDB operations on the table
        try:
            slots = handler_input.request_envelope.request.intent.slots
            word = slots['anything']
            if word.value:
                speak_output=word.value;
            else:
                speak_output="null"

            dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('skills-words')

            response1 = table.scan()
            response2 = table.put_item(
            Item={
               'words': word.value,
               'value': word.value
            }
            )

        except Exception as e:
            # Exception handling
            raise e
        # continue . .
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


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
        # logger.error(exception, exc_info=True)

        # speak_output = "Sorry, I had trouble doing what you asked. Please try again."
        speak_output = "null in exception";
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("ask for input")
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())

sb.add_request_handler(RecordIntentHandler())

sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()


# sb.add_request_handler(HelpIntentHandler())
# sb.add_request_handler(CancelOrStopIntentHandler())
# sb.add_request_handler(FallbackIntentHandler())
# sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers


# class HelloWorldIntentHandler(AbstractRequestHandler):
#     """Handler for Hello World Intent."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         speak_output = "Hello World!"

#         return (
#             handler_input.response_builder
#                 .speak(speak_output)
#                 # .ask("add a reprompt if you want to keep the session open for the user to respond")
#                 .response
#         )


# class HelpIntentHandler(AbstractRequestHandler):
#     """Handler for Help Intent."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         speak_output = "You can say hello to me! How can I help?"

#         return (
#             handler_input.response_builder
#                 .speak(speak_output)
#                 .ask(speak_output)
#                 .response
#         )


# class CancelOrStopIntentHandler(AbstractRequestHandler):
#     """Single handler for Cancel and Stop Intent."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
#                 ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         speak_output = "Goodbye!"

#         return (
#             handler_input.response_builder
#                 .speak(speak_output)
#                 .response
#         )

# class FallbackIntentHandler(AbstractRequestHandler):
#     """Single handler for Fallback Intent."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         logger.info("In FallbackIntentHandler")
#         speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
#         reprompt = "I didn't catch that. What can I help you with?"

#         return handler_input.response_builder.speak(speech).ask(reprompt).response

# class SessionEndedRequestHandler(AbstractRequestHandler):
#     """Handler for Session End."""
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response

#         # Any cleanup logic goes here.

#         return handler_input.response_builder.response


# class IntentReflectorHandler(AbstractRequestHandler):
#     """The intent reflector is used for interaction model testing and debugging.
#     It will simply repeat the intent the user said. You can create custom handlers
#     for your intents by defining them above, then also adding them to the request
#     handler chain below.
#     """
#     def can_handle(self, handler_input):
#         # type: (HandlerInput) -> bool
#         return ask_utils.is_request_type("IntentRequest")(handler_input)

#     def handle(self, handler_input):
#         # type: (HandlerInput) -> Response
#         intent_name = ask_utils.get_intent_name(handler_input)
#         speak_output = "You just triggered " + intent_name + "."

#         return (
#             handler_input.response_builder
#                 .speak(speak_output)
#                 # .ask("add a reprompt if you want to keep the session open for the user to respond")
#                 .response
#         )


