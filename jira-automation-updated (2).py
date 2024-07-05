from jira import JIRA
from jira.exceptions import JIRAError

# Static project and issue keys
EPIC_PROJECT_KEY = "10267"
STORY_PROJECT_KEYS = [
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10091",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: vig-app-prod\nImage Name: mgmt-entities-loader\nAge in Days: 486\nOwner: VigApp\n",
        "owner": "VigApp",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10092",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: vig-app-prod\nImage Name: vig-app-backend\nAge in Days: 486\nOwner: VigApp\n",
        "owner": "VigApp",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10093",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: vig-app-prod\nImage Name: vig-app-frontend-react\nAge in Days: 486\nOwner: VigApp\n",
        "owner": "VigApp",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10094",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: agent-files-gateway-prod\nImage Name: agent-files-gateway\nAge in Days: 493\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10095",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: apicurio-prod\nImage Name: apicurio-v225\nAge in Days: 468\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10096",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ares-prod-gov\nImage Name: apollo-dmux\nAge in Days: 1364\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10097",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: hermes-json-encoder-prod\nImage Name: hermes-json-encoder\nAge in Days: 960\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10098",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: hermes-prod\nImage Name: hermes-api\nAge in Days: 1365\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10099",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: kafka-connect-s3-prod\nImage Name: kafka-connect-s3\nAge in Days: 958\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10100",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: perseus-prod-gov\nImage Name: apollo-dmux\nAge in Days: 1137\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10101",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-data-collector-prod\nImage Name: reputation-data-collector\nAge in Days: 460\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10102",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-connect-prod\nImage Name: kafka-connect-v624\nAge in Days: 469\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10103",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-sighting-logger-prod\nImage Name: reputation-sighting-logger\nAge in Days: 461\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10104",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-sightings-provider-prod\nImage Name: reputation-sightings-provider\nAge in Days: 460\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10105",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-verdict-calculator-service-prod\nImage Name: reputation-verdict-calculator-service\nAge in Days: 460\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10106",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-verdict-modifier-prod\nImage Name: reputation-verdict-modifier\nAge in Days: 460\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10107",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-verdict-provider-prod\nImage Name: reputation-verdict-provider\nAge in Days: 460\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10108",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: scalyr-star-prod\nImage Name: scalyr-star-control-plane\nAge in Days: 448\nOwner: bd-infra\n",
        "owner": "bd-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10109",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cloud-funnel-control-plane-prod\nImage Name: service-api\nAge in Days: 439\nOwner: bigdata\n",
        "owner": "bigdata",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10110",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cloud-data-services-prod\nImage Name: mgmt-entities-loader\nAge in Days: 619\nOwner: common-platform-services\n",
        "owner": "common-platform-services",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10111",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: toggle-service-prod\nImage Name: mgmt-entities-loader\nAge in Days: 622\nOwner: common-platform-services\n",
        "owner": "common-platform-services",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10112",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: toggle-service-prod\nImage Name: service-api\nAge in Days: 622\nOwner: common-platform-services\n",
        "owner": "common-platform-services",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10113",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: atlas-cm-service-prod\nImage Name: atlas-cm-service\nAge in Days: 871\nOwner: cps-infra\n",
        "owner": "cps-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10114",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: file-services-prod\nImage Name: file-services\nAge in Days: 359\nOwner: cps-infra\n",
        "owner": "cps-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10115",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: file-services-prod\nImage Name: nginx-prometheus-exporter\nAge in Days: 359\nOwner: cps-infra\n",
        "owner": "cps-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10116",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: file-services-prod\nImage Name: ubuntu\nAge in Days: 359\nOwner: cps-infra\n",
        "owner": "cps-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10117",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-cassandra-prod\nImage Name: cass-operator\nAge in Days: 455\nOwner: dbap\n",
        "owner": "dbap",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10118",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-cassandra-prod\nImage Name: cassandra-reaper\nAge in Days: 282\nOwner: dbap\n",
        "owner": "dbap",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10119",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cert-manager\nImage Name: cert-manager-cainjector\nAge in Days: 321\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10120",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cert-manager\nImage Name: cert-manager-controller\nAge in Days: 321\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10121",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cert-manager\nImage Name: cert-manager-webhook\nAge in Days: 321\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10122",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ebs-controller\nImage Name: livenessprobe\nAge in Days: 367\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10123",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: external-secrets\nImage Name: kubernetes-external-secrets\nAge in Days: 363\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10124",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: gha-sentinel-general-use-runner\nImage Name: kube-rbac-proxy\nAge in Days: 217\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10125",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: gha-sentinel-iac-runner\nImage Name: kube-rbac-proxy\nAge in Days: 217\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10126",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: gha-sentinel-iam-runner\nImage Name: kube-rbac-proxy\nAge in Days: 196\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10127",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: kube-system\nImage Name: cluster-autoscaler\nAge in Days: 1065\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10128",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: kube-system\nImage Name: cluster-proportional-autoscaler\nAge in Days: 1065\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10129",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: kube-system\nImage Name: coredns\nAge in Days: 1065\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10130",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: kubernetes-dashboard\nImage Name: dashboard\nAge in Days: 1065\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10131",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: kubernetes-dashboard\nImage Name: metrics-scraper\nAge in Days: 1065\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10132",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: logstash\nImage Name: logstash-exporter\nAge in Days: 413\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10133",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: sealed-secrets\nImage Name: sealed-secrets-controller\nAge in Days: 1063\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10134",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: spark-operator\nImage Name: s1-spark-operator\nAge in Days: 247\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10135",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: traefik-external\nImage Name: traefik\nAge in Days: 681\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10136",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: traefik-internal\nImage Name: traefik\nAge in Days: 1065\nOwner: devops\n",
        "owner": "devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10137",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: eventdb-coordinator-prod\nImage Name: mgmt-entities-loader\nAge in Days: 478\nOwner: dpcs\n",
        "owner": "dpcs",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10138",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: eventdb-coordinator-prod\nImage Name: service-api\nAge in Days: 483\nOwner: dpcs\n",
        "owner": "dpcs",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10139",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: query-gateway-prod\nImage Name: query-gateway\nAge in Days: 1576\nOwner: dpcs\n",
        "owner": "dpcs",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10140",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-ops-forensics-mms-prod\nImage Name: mgmt-entities-loader\nAge in Days: 155\nOwner: elabs\n",
        "owner": "elabs",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10141",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-ops-mms-prod\nImage Name: mgmt-entities-loader\nAge in Days: 114\nOwner: elabs\n",
        "owner": "elabs",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10142",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-ops-mms-prod\nImage Name: scheduler\nAge in Days: 101\nOwner: elabs\n",
        "owner": "elabs",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10143",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: doppler-listener\nImage Name: doppler-listener\nAge in Days: 185\nOwner: embedded-devops\n",
        "owner": "embedded-devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10144",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: fedramp-replication-gov-prod\nImage Name: docker\nAge in Days: 377\nOwner: embedded-devops\n",
        "owner": "embedded-devops",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10145",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-upgrade-policy-prod\nImage Name: activities-manager\nAge in Days: 493\nOwner: epps\n",
        "owner": "epps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10146",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-upgrade-policy-prod\nImage Name: maintenance-manager\nAge in Days: 493\nOwner: epps\n",
        "owner": "epps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10147",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-upgrade-policy-prod\nImage Name: maintenance-worker\nAge in Days: 493\nOwner: epps\n",
        "owner": "epps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10148",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-upgrade-policy-prod\nImage Name: mgmt-entities-loader\nAge in Days: 493\nOwner: epps\n",
        "owner": "epps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10149",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-upgrade-policy-prod\nImage Name: service-api\nAge in Days: 493\nOwner: epps\n",
        "owner": "epps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10150",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-console-shared-0-kafka-prod\nImage Name: cert-update\nAge in Days: 157\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10151",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-console-shared-0-kafka-prod\nImage Name: kafka\nAge in Days: 785\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10152",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-console-shared-0-kafka-prod\nImage Name: kafka-lag-exporter\nAge in Days: 497\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10153",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-console-shared-0-kafka-prod\nImage Name: kafka-prometheus-jmx-exporter\nAge in Days: 497\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10154",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-console-shared-0-kafka-prod\nImage Name: strimzi-operator\nAge in Days: 157\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10155",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-console-shared-0-kafka-prod\nImage Name: user-secret-sync\nAge in Days: 157\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10156",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-entities-stream-kafka-prod\nImage Name: cert-update\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10157",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-entities-stream-kafka-prod\nImage Name: kafka\nAge in Days: 1137\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10158",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-entities-stream-kafka-prod\nImage Name: kafka-lag-exporter\nAge in Days: 500\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10159",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-entities-stream-kafka-prod\nImage Name: kafka-prometheus-jmx-exporter\nAge in Days: 500\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10160",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-entities-stream-kafka-prod\nImage Name: strimzi-operator\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10161",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-entities-stream-kafka-prod\nImage Name: user-secret-sync\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10162",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-kafka-prod\nImage Name: cert-update\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10163",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-kafka-prod\nImage Name: kafka\nAge in Days: 1357\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10164",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-kafka-prod\nImage Name: kafka-lag-exporter\nAge in Days: 497\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10165",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-kafka-prod\nImage Name: kafka-prometheus-jmx-exporter\nAge in Days: 497\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10166",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-kafka-prod\nImage Name: strimzi-operator\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10167",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-kafka-prod\nImage Name: user-secret-sync\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10168",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mms-kafka-prod\nImage Name: cert-update\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10169",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mms-kafka-prod\nImage Name: kafka\nAge in Days: 1357\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10170",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mms-kafka-prod\nImage Name: kafka-lag-exporter\nAge in Days: 500\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10171",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mms-kafka-prod\nImage Name: kafka-prometheus-jmx-exporter\nAge in Days: 500\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10172",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mms-kafka-prod\nImage Name: strimzi-operator\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10173",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mms-kafka-prod\nImage Name: user-secret-sync\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10174",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: perseus-kafka-prod\nImage Name: cert-update\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10175",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: perseus-kafka-prod\nImage Name: kafka\nAge in Days: 1142\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10176",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: perseus-kafka-prod\nImage Name: kafka-lag-exporter\nAge in Days: 497\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10177",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: perseus-kafka-prod\nImage Name: kafka-prometheus-jmx-exporter\nAge in Days: 497\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10178",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: perseus-kafka-prod\nImage Name: strimzi-operator\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10179",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: perseus-kafka-prod\nImage Name: user-secret-sync\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10180",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-kafka-prod\nImage Name: cert-update\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10181",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-kafka-prod\nImage Name: kafka\nAge in Days: 1137\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10182",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-kafka-prod\nImage Name: kafka-lag-exporter\nAge in Days: 500\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10183",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-kafka-prod\nImage Name: kafka-prometheus-jmx-exporter\nAge in Days: 500\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10184",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-kafka-prod\nImage Name: strimzi-operator\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10185",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-kafka-prod\nImage Name: user-secret-sync\nAge in Days: 156\nOwner: fedramp-sre\n",
        "owner": "fedramp-sre",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10186",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: license-service-prod\nImage Name: mgmt-entities-loader\nAge in Days: 275\nOwner: fleet-management\n",
        "owner": "fleet-management",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10187",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: license-service-prod\nImage Name: service-api\nAge in Days: 275\nOwner: fleet-management\n",
        "owner": "fleet-management",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10188",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: atlas-auth-service-prod\nImage Name: atlas-auth-service\nAge in Days: 871\nOwner: iam-team\n",
        "owner": "iam-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10189",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: identity-provider-service-prod\nImage Name: authentication-service\nAge in Days: 97\nOwner: iam-team\n",
        "owner": "iam-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10190",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: identity-provider-service-prod\nImage Name: authorization-service\nAge in Days: 274\nOwner: iam-team\n",
        "owner": "iam-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10191",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: identity-provider-service-prod\nImage Name: mgmt-entities-loader\nAge in Days: 274\nOwner: iam-team\n",
        "owner": "iam-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10192",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: identity-provider-service-prod\nImage Name: sql-metrics-exporter\nAge in Days: 97\nOwner: iam-team\n",
        "owner": "iam-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10193",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: identity-provider-service-prod\nImage Name: trust-service\nAge in Days: 274\nOwner: iam-team\n",
        "owner": "iam-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10194",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: traefik-internal\nImage Name: external-autoscaler\nAge in Days: 375\nOwner: infra\n",
        "owner": "infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10195",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-console-shared-0-kafka-prod\nImage Name: akhq\nAge in Days: 423\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10196",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-entities-stream-kafka-prod\nImage Name: akhq\nAge in Days: 423\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10197",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-kafka-prod\nImage Name: akhq\nAge in Days: 449\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10198",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mms-kafka-prod\nImage Name: akhq\nAge in Days: 500\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10199",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: monitoring\nImage Name: cert-exporter-v211\nAge in Days: 388\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10200",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: monitoring\nImage Name: kube-state-metrics\nAge in Days: 495\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10201",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: monitoring\nImage Name: nginx\nAge in Days: 484\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10202",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: observability\nImage Name: prometheus-operator\nAge in Days: 548\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10203",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: perseus-kafka-prod\nImage Name: akhq\nAge in Days: 497\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10204",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-kafka-prod\nImage Name: akhq\nAge in Days: 500\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10205",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-prod\nImage Name: akhq\nAge in Days: 469\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10206",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-prod\nImage Name: cert-update\nAge in Days: 156\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10207",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-prod\nImage Name: kafka\nAge in Days: 469\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10208",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-prod\nImage Name: kafka-lag-exporter\nAge in Days: 469\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10209",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-prod\nImage Name: kafka-prometheus-jmx-exporter\nAge in Days: 469\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10210",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-prod\nImage Name: strimzi-operator\nAge in Days: 156\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10211",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-prod\nImage Name: user-secret-sync\nAge in Days: 156\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10212",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: s1-kafka-api-prod\nImage Name: s1-kafka-api\nAge in Days: 157\nOwner: infra-apps\n",
        "owner": "infra-apps",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10213",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cert-manager\nImage Name: cert-manager-cainjector\nAge in Days: 255\nOwner: kaass\n",
        "owner": "kaass",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10214",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cert-manager\nImage Name: cert-manager-controller\nAge in Days: 255\nOwner: kaass\n",
        "owner": "kaass",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10215",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cert-manager\nImage Name: cert-manager-webhook\nAge in Days: 255\nOwner: kaass\n",
        "owner": "kaass",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10216",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ebs-csi\nImage Name: livenessprobe\nAge in Days: 363\nOwner: kaass\n",
        "owner": "kaass",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10217",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: external-dns-internal\nImage Name: external-dns\nAge in Days: 111\nOwner: kaass\n",
        "owner": "kaass",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10218",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: spark-operator\nImage Name: spark-operator\nAge in Days: 129\nOwner: kaass\n",
        "owner": "kaass",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10219",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: activity-task-transformer\nAge in Days: 156\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10220",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: callback\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10221",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: commands-publisher\nAge in Days: 156\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10222",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: data-plane\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10223",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: marketplace-fe\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10224",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: pushgateway\nAge in Days: 156\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10225",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: scope-lifecycle-handler\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10226",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: scope-lifecycle-orchestrator\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10227",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: task-executor\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10228",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: task-filter\nAge in Days: 156\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10229",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: task-scheduler\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10230",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: telemetry\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10231",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: transporter\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10232",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: trigger-task-transformer\nAge in Days: 156\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10233",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: users-manager\nAge in Days: 156\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10234",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: vendor-catalog\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10235",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: xdr-hub-fe\nAge in Days: 155\nOwner: marketplace\n",
        "owner": "marketplace",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10236",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: dataset-support\nAge in Days: 156\nOwner: marketplace-platform\n",
        "owner": "marketplace-platform",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10237",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: mgmt-entities-loader\nAge in Days: 156\nOwner: marketplace-platform\n",
        "owner": "marketplace-platform",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10238",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: nexus-store\nAge in Days: 156\nOwner: marketplace-platform\n",
        "owner": "marketplace-platform",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10239",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: event-gateway-prod\nImage Name: event-gateway\nAge in Days: 469\nOwner: mgmt\n",
        "owner": "mgmt",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10240",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: atlas-backend-prod\nImage Name: service-api\nAge in Days: 619\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10241",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cloud-data-services-prod\nImage Name: mgmt-command-service\nAge in Days: 106\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10242",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: cloud-data-services-prod\nImage Name: sentinel-cloud\nAge in Days: 106\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10243",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-cleaner-signing-service-prod\nImage Name: service-api\nAge in Days: 486\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10244",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: alertmanager\nAge in Days: 158\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10245",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: faas-netes\nAge in Days: 158\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10246",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: nats-streaming\nAge in Days: 158\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10247",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: openfaas-function-controller\nAge in Days: 158\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10248",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: prometheus\nAge in Days: 158\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10249",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-nexus-prod\nImage Name: queue-worker\nAge in Days: 158\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10250",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-ops-forensics-mms-prod\nImage Name: forensics-api\nAge in Days: 155\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10251",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-ops-forensics-mms-prod\nImage Name: forensics-event-handler\nAge in Days: 155\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10252",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-ops-mms-prod\nImage Name: mms-event-handler\nAge in Days: 114\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10253",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-ops-mms-prod\nImage Name: service-api\nAge in Days: 143\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10254",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-scripts-prod\nImage Name: mgmt-entities-loader\nAge in Days: 476\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10255",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-scripts-prod\nImage Name: rso-api\nAge in Days: 476\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10256",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: remote-scripts-prod\nImage Name: rso-event-handler\nAge in Days: 476\nOwner: mgmt-cloud-data\n",
        "owner": "mgmt-cloud-data",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10257",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-assets-prod\nImage Name: ranger-configuration\nAge in Days: 650\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10258",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-fingerprint-prod\nImage Name: ranger-fingerprint\nAge in Days: 645\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10259",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: care\nAge in Days: 468\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10260",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: command-engine\nAge in Days: 468\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10261",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: cpe-resolver\nAge in Days: 468\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10262",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: cve-enrichment\nAge in Days: 297\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10263",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: data-receiver\nAge in Days: 465\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10264",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: labels-processing\nAge in Days: 650\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10265",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: ranger-scheduler\nAge in Days: 468\nOwner: mgmt-ranger\n",
        "owner": "mgmt-ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10266",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: mgmt-entities-loader\nAge in Days: 469\nOwner: ranger\n",
        "owner": "ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10267",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: persistence\nAge in Days: 468\nOwner: ranger\n",
        "owner": "ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10268",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: ranger-api\nAge in Days: 469\nOwner: ranger\n",
        "owner": "ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10269",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: ranger-pipeline-prod\nImage Name: vulnerability-enrichment\nAge in Days: 468\nOwner: ranger\n",
        "owner": "ranger",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10270",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: identity-provider-service-prod\nImage Name: ubuntu\nAge in Days: 274\nOwner: saas-infra\n",
        "owner": "saas-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10271",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mms-gw-static-network-prod\nImage Name: ubuntu\nAge in Days: 465\nOwner: saas-infra\n",
        "owner": "saas-infra",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10272",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-tag-manager-prod\nImage Name: commands-publisher\nAge in Days: 148\nOwner: spp-team\n",
        "owner": "spp-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10273",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-tag-manager-prod\nImage Name: mgmt-api\nAge in Days: 149\nOwner: spp-team\n",
        "owner": "spp-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10274",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-tag-manager-prod\nImage Name: mgmt-entities-loader\nAge in Days: 148\nOwner: spp-team\n",
        "owner": "spp-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10275",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-threat-actions-prod\nImage Name: callbacks-manager\nAge in Days: 135\nOwner: spp-team\n",
        "owner": "spp-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10276",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-threat-actions-prod\nImage Name: commands-publisher\nAge in Days: 135\nOwner: spp-team\n",
        "owner": "spp-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10277",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-threat-actions-prod\nImage Name: mgmt-entities-loader\nAge in Days: 135\nOwner: spp-team\n",
        "owner": "spp-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10278",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-threat-actions-prod\nImage Name: service-api\nAge in Days: 135\nOwner: spp-team\n",
        "owner": "spp-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10279",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-threat-actions-prod\nImage Name: triggers-manager\nAge in Days: 135\nOwner: spp-team\n",
        "owner": "spp-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10280",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: reputation-kafka-connect-prod\nImage Name: kafka-connect-ui-v097\nAge in Days: 468\nOwner: sre-shared-services\n",
        "owner": "sre-shared-services",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10281",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-prod\nImage Name: alerts-manager\nAge in Days: 99\nOwner: star-team\n",
        "owner": "star-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10282",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-prod\nImage Name: commands-publisher\nAge in Days: 99\nOwner: star-team\n",
        "owner": "star-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10283",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-prod\nImage Name: mgmt-api\nAge in Days: 99\nOwner: star-team\n",
        "owner": "star-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10284",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-prod\nImage Name: mgmt-entities-loader\nAge in Days: 99\nOwner: star-team\n",
        "owner": "star-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    },
    {
        "project": "FEDRAMP-10090",
        "issue_key": "FEDRAMP-10285",
        "summary": "Clone of FEDRAMP-10091",
        "description": "\nNamespace: mgmt-war-prod\nImage Name: rules-manager\nAge in Days: 99\nOwner: star-team\n",
        "owner": "star-team",
        "epic_key": "FEDRAMP-10091",
        "clone_links": true
    }
], basic_auth=(jira_token['username'], jira_token['credential']), options={'server': 'https://sentinelone.atlassian.net/', 'server_info': {'server_url': 'https://sentinelone.atlassian.net/'}})

        # Prompt user for PI variable
        pi_variable = input("Enter the value for PI: ")

        # Create Epic
        epic_summary = f"Base Image Uplift - {pi_variable}"
        epic = jira.create_issue(project=EPIC_PROJECT_KEY, summary=epic_summary, issuetype={'name': 'Epic'})

        # Echo the name of the created epic
        print(f"Epic created: {epic.key} - {epic_summary}")

        # Iterate through each component and clone stories
        for component, details in STORY_PROJECT_KEYS.items():
            project_key = details["project"]
            issue_key = details["issue_key"]
            print(f"Cloning story for {component} (Issue Key: {issue_key}) in Project: {project_key}...")

            # Clone the issue from the specified project and clone it into the same project
            original_issue = jira.issue(issue_key)

            # Extract the value of the ;labels and 'Team' field
            labels = original_issue.fields.labels
            team_field_value = original_issue.fields.customfield_11067
            team_field = {"id": team_field_value.id, "value": team_field_value.value}

            # Create the new issue and set the custom field value, summary
            cloned_issue = jira.create_issue(
                summary=f"{component} - Base Image Update Required - FedRAMP Deployment Ticket Request",
                description="The base image for this component is out-of-date. To mitigate vulnerabilities and remain within FedRAMP policy compliance, these base images should be updated at least once per month. Please provide FedRAMP with a new build of the component on the latest base image and submit a FedRAMP deployment ticket with the details for that new version. The template to be used for that deployment ticket is located here:\n\nFEDRAMP-2764: [TEMPLATE][FedRAMP Deployment] <deployable unit> - <version>\n\nPlease reach out to Tim Levesque, Barry Berard, or Joel Stewart if you have any questions.",
                project=project_key,
                issuetype={'name': 'Story'},
                customfield_11067=team_field,
                labels=labels
            )
             # Add the label "FRH-BaseImage" to the cloned ticket
            jira.add_issues_to_epic(epic.key, [cloned_issue.key])

            # Link cloned issue to the epic
            print(f"Cloned Story: {cloned_issue.key} - {cloned_issue.fields.summary}")

            # Set the Parent Link field for the cloned ticket to the epic
            jira.create_issue_link('is child of', cloned_issue, epic)

            # Ask user if they want to continue with the next component, skip, or stop - This can be uncommented for troubleshooting.
            #continue_script = input("Do you want to continue with the next component (Y), skip the next component (S), or stop (N)? ").strip().upper()
            #if continue_script == 'S':
            #    print("Skipping the next component.")
            #    continue  # Skip the next component and continue with the loop
            #elif continue_script == 'N':
            #    print("Stopping the script.")
            #    break  # Exit the loop if the user wants to stop

    except JIRAError as e:
        print(f"Jira API call failed. Error: {e}")

if __name__ == "__main__":
    create_epic_and_clone_stories()
