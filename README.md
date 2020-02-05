# Inheritance-and-Anonymous-Classes-with-Pyjnius

### Java-Code for Custom WebViewClient

```Java
package com.my.webview;

import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MyWebViewClient extends WebViewClient {
    private String script;

    public String getScript() {
        return this.script;
    }

    public void setScript(String script) {
        this.script = script;
    }

    @Override
    public void onPageFinished(WebView view, String url) {
        view.loadUrl(this.script);
    }
}
```
Refereced Library: android.jar (Android\Sdk\platforms\android-27\android.jar)

One can then use the (anonymous-)classes in the generated .jar of the Java project within Python using jnius.
```Python
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
```
