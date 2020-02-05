from jnius import autoclass, cast
from android.runnable import run_on_ui_thread

activity = autoclass("org.kivy.android.PythonActivity").mActivity
context = cast("android.content.Context", activity.getApplicationContext())
WV = autoclass("android.webkit.WebView")
WVC = autoclass("com.my.webview.MyWebViewClient")
ChromeClient = autoclass("android.webkit.WebChromeClient")


class WebClient:

    #runs a ChromeClient on the (main-)activity
    @run_on_ui_thread
    def go(url, script):
        #get settings
        webview = WV(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.setWebChromeClient(ChromeClient())
        wvc = WVC()
        #script runs after load
        wvc.setScript(script)
        webview.setWebViewClient(wvc)
        activity.setContentView(webview)
        webview.loadUrl(url)
