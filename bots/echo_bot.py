# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount


class EchoBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_input = turn_context.activity.text.strip().lower()

        if user_input == "hello":
            await turn_context.send_activity("Hi there! How can I assist you today?")
        elif user_input == "help":
            await turn_context.send_activity("I can reverse your message, greet you, or respond to simple prompts like 'hello'.")
        elif user_input == "":
            await turn_context.send_activity("You didn’t type anything. Please try again.")
        else:
            reversed_text = user_input[::-1]
            await turn_context.send_activity(f"Reversed: {reversed_text}")

