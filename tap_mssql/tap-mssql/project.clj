(defproject tap-mssql
  "1.6.2"
  :description "Singer.io tap for extracting data from a Microsft SQL Server "
  :url "https://github.com/stitchdata/tap-mssql"
  :license {:name "GNU Affero General Public License Version 3; Other commercial licenses available."
            :url "https://www.gnu.org/licenses/agpl-3.0.en.html"}
  :dependencies [[org.clojure/clojure "1.9.0"]
                 [org.clojure/tools.cli "0.4.1"]
                 [org.clojure/data.json "0.2.6"]

                 ;; jdbc
                 [org.clojure/java.jdbc "0.7.9"]
                 [com.microsoft.sqlserver/mssql-jdbc "7.2.1.jre8"]

                 ;; logging
                 [org.clojure/tools.logging "0.3.1"]
                 [log4j "1.2.17" :exclusions [javax.mail/mail
                                              javax.jms/jms
                                              com.sun.jdmk/jmxtools
                                              com.sun.jmx/jmxri]]
                 ;; repl
                 [org.clojure/tools.nrepl "0.2.13"]
                 [cider/cider-nrepl "0.17.0"]

                 ;; test
                 [org.clojure/data.generators "0.1.2"]
                 ]
  :plugins [[lein-pprint "1.2.0"]]
  :main tap-mssql.core
  :profiles {:uberjar {:aot [tap-mssql.core]}
            })
