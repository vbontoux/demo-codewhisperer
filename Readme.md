
# CodeWhisperer Quick demo

## How to install?

- [Setting up CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/setting-up.html):
  - Chose your IDE
  - Exemple with Visual Code: [Installing the AWS Toolkit for Visual Studio Code - AWS Toolkit for VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html)
  - [Authenticating with CodeWhisperer and AWS Toolkit - CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/codewhisperer-auth.html) as :
    - Individual developer with builder ID (does not require an AWS account)
    - Professional-tier developer with AWS IAM Identity Center
    - In-console developer (using AWS Cloud 9, Lambda, or Amazon Sagemaker Studio)

- Setting up this demo code:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Why CodeWhisperer?

- Shortage of developers
- Time spent on undiferentiated code
- Time spent learning APIs, technologies, best practices
- Bias avoidance
  - data privacy (sharing code through developer forums)
  - Approrpriate use of open source (inadvertent copying of code that may unintentionally violate open source)
- write secure code

## CodeWhisperer Features

- Real-time code suggestions
- Scanning for security vulnerabilities includes for example, top 10 in the Open Worldwide Application Security Project (OWASP) standards, enforcement of crypto library and AWS security standards and best practices, and more
- Reference tracking : refrences to sources => information about the licences
- [Language and IDE support in Amazon CodeWhisperer - CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/language-ide-support.html) :
  - High accuracy : Java, Python, JavaScript, TypeScript, C#
  - Less accuracy : Ruby, Go, PHP, C++, C, Shell, Scala, Rust, Kotlin, SQL
  - IDEs : VS Code, JetBrains IDEs (IntelliJ IDEA, PyCharm, CLion, GoLand, WebStorm, Rider, PhpStorm, RubyMine, DataGrip), SageMaker Studio and jupyterlab, AWS Cloud9 and AWS Lambda console

## CodeWhisperer Questions

- [Billing for CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/billing.html)
  - The **individual tier** is free and easy to set up, but does not include the benefits of organizational license management
  - The **professional tier** includes a charge for additional features. Your employer pays the bill through their company AWS account.
- [Sharing your data with AWS](https://docs.aws.amazon.com/codewhisperer/latest/userguide/sharing-data.html)
- [FAQ](https://aws.amazon.com/fr/codewhisperer/faqs/)

## CodeWisperer User Guide

- [What is CodeWhisperer?](https://docs.aws.amazon.com/codewhisperer/latest/userguide/what-is-cwspr.html)
- [Code examples](https://docs.aws.amazon.com/codewhisperer/latest/userguide/whisper-code-examples.html)

## CodeWisperer Workshops

- [Amazon CodeWhisperer Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/6838a1a5-4516-4153-90ce-ac49ca8e1357/en-US)

## Tips

- Security scanning [video](https://youtu.be/GkZ4bT4DMwU)
- Suggestions [Video](https://www.youtube.com/watch?v=qu67bvH2Y08)
  - Use arrows to switch suggetions
  - If a suggestion reffers to a licensed code it appears on top of the suggested code and if you accept it, it is then visible in the reference log console of your IDE
  - you can disable whisperer auto suggestion from AWS tool kit and ure [Option] + [C] to force use

## CodeWhisperer Examples

- Code Whisperer reference log : type *#implement a function to create a simple dynomodb table* and enter + right arrow to get the MIT code sample. This will display a message in the *Codewhisperer reference log* console

```python
#implement a function to create a simple dynomodb table
def create_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='my-first-table',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table
```

- Security scan : type the below code and go to the AWS visual studio menu en click *Run Security Scan*

```python
import logging
import psycopg2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="XXXXXXXX",
        password="XXXXXXXX"
    )
```
