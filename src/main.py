#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2, currency_rates, logging

class Main(webapp2.RequestHandler):
    def get(self):
        html = """
<!DOCTYPE html>
<html dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Rate de schimb cu API JSON/JSONP</title>
        <link rel="stylesheet" media="all" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css"/>
        <link rel="stylesheet" media="all" href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css"/>
        <link href="http://fonts.googleapis.com/css?family=Ubuntu:400,700&subset=latin,latin-ext" rel="stylesheet" type="text/css">
        <style type="text/css">
            body { font: 18px;; font-family: 'Ubuntu', 'Helvetica Neue', Arial; min-height: 600px; padding-top: 10px;}
            h1 { font-weight: bold; }
            p, p > *, ul, li, pre, code, div{ font-size: 18px; }
            .got-error { font-size: 1em; font-family: Verdana; }
            code, code >* { color: #FFFFFF; background: #222222; }
            .examples li{
                margin-bottom: 10px;
            }
            .subheading{
                border-bottom: 1px #dcdcdc solid;
                margin: 25px auto;
            }
        </style>
    </head>
    <body>

        <div class="container">

            <h1 style="text-align: center;"><i class="fa fa-money"></i>  Rate de schimb cu API JSON/JSONP</h1>

            <div id="despre">
                Acesta este un serviciu gratuit care folose&#351;te saitul <a href="http://www.xe.com/">xe.com</a> pentru a extrage cursul valutar &#351;i a face conversii
                &#238;ntre diverse monede. <br/>
                Proiectul este bazat pe cel dezvoltat de <a href="http://rate-exchange.appspot.com/" target="_blank">Hippasus Chu</a>,
                fiind o copie a acestuia &#238;n termeni de func&#355;ionalitate &#351;i este &#238;ntre&#355;inut de <a href="http://adrian.silimon.eu/" target="_blank">Adrian &#350;ilimon</a>.<br/>
                Momentan rezultatele ob&#355;inute &#238;n urma cererilor sunt salvate &#238;ntr-un cache pentru 10 minute, a&#351;adar nu ofer&#259; rezultate instante.

                <p style="text-align: center; margin-top: 10px;">
                    Distribuit sub <a href="http://opensource.org/licenses/MIT" target="_blank">licen&#355;&#259; MIT</a> |
                    <a href="https://github.com/adrian7/ExchangeRates">R&#259;sfoie&#351;te codul pe Github</a>
                </p>

            </div>

            <h3 class="subheading">Documenta&#355;ie</h3>

            <div id="docs">

                <p>
                    <i class="fa fa-align-left"></i> Lista de monede (JSON): <code><a href="$host_url/currencies-en_US.json" target="_blank">$host_url/currencies-en_US.json</a></code>
                </p>

                <p>
                    <i class="fa fa-terminal"></i> HTTP URI: <code>$host_url/currency</code>
                </p>

                Parametrii:
                <ul>
                    <li><em>from</em> : codul monedei din care se face conversia</li>
                    <li><em>to</em> : codul monedei la care se face conversia</li>
                    <li><em>q</em> : suma de convertit (op&#355;ional)</li>
                    <li><em>callback</em> : functia JS care va fi chemat&#259; cu obiectul rezultat (op&#355;ional)</li>
                </ul>

                R&#259;spuns - sub forma unui obiect JSON:<br/>
                <pre>{
"to": "EUR", //moneda din care se face conversia
"rate": 0.77966630299999995, //rata de schimb
"from": "USD",   //moneda la care se face conversia
"v": 1.5593326059999999 //valoarea convertita la noua moned&#259;
}</pre>

                <br/><br/>
                Exemple:
                <ul class="examples">
                    <li>Ia cursul valutar din RON la USD:
                        <code>
                            <a href="$host_url/currency?from=RON&to=USD&q=1" target="_blank" rel="nofollow">$host_url/currency?from=RON&to=USD&q=1</a>
                        </code>
                    </li>
                    <li>
                        Converte&#351;te 200 RON &#238;n EUR:
                        <code>
                            <a href="$host_url/currency?from=RON&to=EUR&q=200" target="_blank" rel="nofollow">$host_url/currency?from=RON&to=EUR&q=200</a>
                        </code>
                    </li>
                    <li>
                        Converte&#351;te 350 de USD in RON &#351;i cheam&#259; functia JS <em>myFunction</em> cu obiectul rezultat: <br/>
                        <code style="margin-top: 5px;">
                            <a href="$host_url/currency?from=USD&to=RON&q=350&callback=myFunction" target="_blank" rel="nofollow">$host_url/currency?from=USD&to=RON&q=350&callback=myFunction</a>
                        </code>
                    </li>
                </ul>

                <br/>

                <br/>

            </div>

            <h3 class="subheading">Proiecte care folosesc serviciul</h3>
            <div>
                <p style="text-align: center">
                    <a href="http://finflow.org/">
                        <img src="http://finflow.org/images/finflow.png" height="50"/><br/> FinFlow - asistentul t&#259;u financiar
                    </a>
                </p>
            </div>

        </div>
        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"/>
        <script type="text/javascript" src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"/>
    </body>
</html>
        """
        
        html = html.replace('$host_url', self.request.host_url)
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)

app = webapp2.WSGIApplication([('/', Main), ('/currency', currency_rates.CurrencyRates)])