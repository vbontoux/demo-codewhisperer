
# CodeWhisperer Quick demo

## Why ?

- Shortage of developers
- Time spent on undiferentiated code
- Time spent learning APIs, technologies, best practices
- Bias avoidance
  - data privacy (sharing code through developer forums)
  - Approrpriate use of open source (inadvertent copying of code that may unintentionally violate open source)
- write secure code

## Features

- Real-time code suggestions
- Scanning for security vulnerabilities includes for example, top 10 in the Open Worldwide Application Security Project (OWASP) standards, enforcement of crypto library and AWS security standards and best practices, and more
- Reference tracking : refrences to sources => information about the licences
- [Language and IDE support in Amazon CodeWhisperer - CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/language-ide-support.html) : 
  - High accuracy : Java, Python, JavaScript, TypeScript, C#
  - Less accuracy : Ruby, Go, PHP, C++, C, Shell, Scala, Rust, Kotlin, SQL
  - IDEs : VS Code, JetBrains IDEs (IntelliJ IDEA, PyCharm, CLion, GoLand, WebStorm, Rider, PhpStorm, RubyMine, DataGrip), SageMaker Studio and jupyterlab, AWS Cloud9 and AWS Lambda console

## Questions

- [Pricing](https://aws.amazon.com/fr/codewhisperer/pricing/)
- [FAQ](https://aws.amazon.com/fr/codewhisperer/faqs/)

## CodeWisperer User Guide

- [What is CodeWhisperer? - CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/what-is-cwspr.html)
- [Code examples - CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/whisper-code-examples.html)

## CodeWisperer Workshops

- [Amazon CodeWhisperer Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/6838a1a5-4516-4153-90ce-ac49ca8e1357/en-US)

## Tips

- Security scanning [video](https://youtu.be/GkZ4bT4DMwU)
- Suggestions [Video](https://www.youtube.com/watch?v=qu67bvH2Y08)
  - Use arrows to switch suggetions
  - If a suggestion reffers to a licensed code it appears on top of the suggested code and if you accept it, it is then visible in the reference log console of your IDE
  - you can disable whisperer auto suggestion from AWS tool kit and ure [Option] + [C] to force use

## Examples

- Code Whisperer reference log : type *#implement a function to create a simple dynomodb table* and enter + right arrow to get the MIT code sample

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
