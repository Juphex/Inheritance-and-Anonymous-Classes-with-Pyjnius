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