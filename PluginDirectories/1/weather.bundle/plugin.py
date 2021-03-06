#!/usr/bin/python

import sys, urllib, os
import AppKit
import i18n

def dark_mode():
    import Foundation
    return Foundation.NSUserDefaults.standardUserDefaults().persistentDomainForName_(Foundation.NSGlobalDomain).objectForKey_("AppleInterfaceStyle") == "Dark"

def use_metric():
    return AppKit.NSLocale.currentLocale().objectForKey_(AppKit.NSLocaleUsesMetricSystem)

def results(parsed, original_query):
    location = parsed['~location']
    title = i18n.localstr('"{0}" weather').format(location)
    html = open(i18n.find_localized_path("weather.html")).read().replace("<!--LOCATION-->", location).replace("<!--UNITS-->", "metric" if use_metric() else "imperial").replace("<!--APPEARANCE-->", "dark" if dark_mode() else "light")
    return {
        "title": title,
        "html": html,
        "webview_transparent_background": True,
        "run_args": location
    }

def run(location):
    os.system('open "http://openweathermap.org/find?q={0}"'.format(urllib.quote(location)))
