from stario import App
from stario import Relay

from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUrlsModule import CHAT_PAGE_URL
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUrlsModule import CHAT_SEND_URL
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUrlsModule import CHAT_SUBSCRIBE_URL
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUrlsModule import CHAT_TYPING_URL
from stariodemo.WebsiteFeatureChatAppPkg.ChatPageEndpointModule import ChatPageEndpoint
from stariodemo.WebsiteFeatureChatAppPkg.SendMessageEndpointModule import SendMessageEndpoint
from stariodemo.WebsiteFeatureChatAppPkg.SubscribeEndpointModule import SubscribeEndpoint
from stariodemo.WebsiteFeatureChatAppPkg.TypingEndpointModule import TypingEndpoint


def ChatAppRegisterEndpoints(app: App, relay: Relay):
    app.get(CHAT_PAGE_URL, ChatPageEndpoint())
    app.get(CHAT_SUBSCRIBE_URL, SubscribeEndpoint(relay))
    app.post(CHAT_SEND_URL, SendMessageEndpoint(relay))
    app.post(CHAT_TYPING_URL, TypingEndpoint(relay))
