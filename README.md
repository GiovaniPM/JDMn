# JDMn
[![JDMn](https://img.shields.io/badge/JDMn-1.0.3-blue.svg)](https://github.com/GiovaniPM/JDMn)

Python/JSON implementation of DMn

## Proposal

To create a lightweight DMn implementation, using a popular file represetantion and a flexible language.
The representative DMn tables, need the complete satisfation of all imput entrys inside the rule to be validate a hypothesis.

## What’s DMN?
This modeling language created by OMG – an international group dedicated to developing technology standards – is a notation for business rules applied to processes.  
DMN makes it so business rules can be transformed into corporate assets, making decision-making and understanding corporate rules easier, which ultimately ensures greater task effectiveness.  
The importance of DMN lies in companies’ need to ensure daily activities are carried out to the letter – that is, in line with what was previously decided.  
In that sense, DMN can turn complex business processes into easy-to-understand models, without omitting any essential rules, clarifying the path being taken for management as well as employees.  
Use of DMN makes it possible for employees and decision-makers to reproduce the same initiatives across departments, optimize communication channels with customers, and improve internal and external analysis.  
With the concept outlined, now let’s move on to how DMN is structured.

## What’s JSON?
JavaScript Object Notation  
The JSON format is syntactically identical to the code for creating JavaScript objects.  
Because of this similarity, a JavaScript program can easily convert JSON data into native JavaScript objects.  
The JSON syntax is derived from JavaScript object notation syntax, but the JSON format is text only. Code for reading and generating JSON data can be written in any programming language.

### Why use JSON instead XML

As a markup language, XML is more complex and requires a tag structure. In contrast, JSON is a data format that extends from JavaScript.  
It does not use tags, which makes it more compact and easier to read for humans. JSON can represent the same data in a smaller file size for faster data transfer.

## What's Python?

Python is a high-level, interpreted programming language with a simple syntax, which makes it easily readable and extremely user- and beginner-friendly. Originally built to satisfy Guido Van Rossum’s desire for a programming language that was simple to use and beautiful to look at, Python was first released to the world in 1991.  
Python also has several other characteristics that make it popular amongst developers and engineers. These include:
- It’s easy to read. Python code uses English keywords rather than punctuation, and its line breaks help define the code blocks. In practice, this means you can identify what the code is designed to do simply by looking at it.
- It’s open source. You can download the source code, modify it, and use it however you want.
- It’s portable. Some languages require you to modify code to run on different platforms, but Python is a cross-platform language, which means you can run the same code on any operating system with a Python interpreter.
- It’s extendable. Python code can be written in other languages (such as C++), and users can add low-level modules to the Python interpreter to customize and optimize their tools.
- It has a broad standard library. This library is available for anyone to access and means that users don’t have to write code for every single function—they can access built-in modules that help with issues in everyday programming and more.

Top 10 Reasons Why Python is So Popular With Developers.

1. Easy to Learn and Use
1. Mature and Supportive Python Community
1. Support from Renowned Corporate Sponsors
1. Hundreds of Python Libraries and Frameworks
1. Versatility, Efficiency, Reliability, and Speed
1. Big data, Machine Learning and Cloud Computing
1. First-choice Language
1. The Flexibility of Python Language
1. Use of python in academics
1. It is interpreted

## So, JSON with Python?

A “JSON object” is very similar to a Python dictionary. A “JSON array” is very similar to a Python list. In the same way that JSON objects can be nested within arrays or arrays nested within objects, Python dictionaries can be nested within lists or lists nested within dictionaries.  
You can save the Python dictionary into JSON files using a built-in module json.

## Software needs

### Python

[![Python](https://img.shields.io/badge/python-3.12.0-brightgreen.svg?logo=python)](https://python.org)

### PIP support

[![Flask](https://img.shields.io/badge/Flask-3.0.0-brightgreen.svg?logo=flask)](https://flask.palletsprojects.com)
[![Flask-Cors](https://img.shields.io/badge/Flask_Cors-4.0.0-brightgreen.svg?logo=python)](https://flask-cors.readthedocs.io/en/latest/)
[![Requests](https://img.shields.io/badge/requests-2.31.0-brightgreen.svg?logo=python)](https://requests.readthedocs.io/en/latest/)
[![uuid](https://img.shields.io/badge/uuid-1.30-brightgreen.svg?logo=python)](https://pypi.org/project/uuid/)
[![wxPython](https://img.shields.io/badge/wxPython-4.2.1-brightgreen.svg?logo=python)](https://wxpython.org/index.html)

### Postman

[![Postman](https://img.shields.io/badge/Postman-10.20.6-brightgreen.svg?logo=postman)](https://www.postman.com/)

### wxFormBuilder

[![wxFormBuilder](https://img.shields.io/badge/wxFormBuilder-4.0.0-brightgreen.svg)](https://github.com/wxFormBuilder/wxFormBuilder/releases/download/v4.0.0/wxFormBuilder-4.0.0-x64.exe)

## Architecture

### How the decision works

The first rule successfully found is our result, regardless of other rules that can be found.  
A successfully rule is the row, wich all columns evaluate with true.  
There are the follow possible data types in input entry: string, date, number and boolean.  
The available logic operators are: <, <=, >, >=, ==, !=, in and not in. Column without a operator will be used ==.

### Project directories

```dos
JDMn (root)
├─── <DIR> api          (api implementation)
├─── <DIR> examples     (json examples)
├─── <DIR> lib          (jdmn library)
├─── <DIR> Setup        (app to create jdmn)
├─── requirements.txt   (pip dependencies file)
└─── README.md          (this file)
```

### File structure

![image](https://github.com/GiovaniPM/JDMn/assets/9011792/038c5661-ae5e-445b-94e8-5878889f0863)

### File example

or.json
```json
{
    "definitions": {
        "decision": {
            "decisionTable": {
                "input": [{
                        "inputExpression": {
                            "label": "colunaUm",
                            "typeRef": "number"
                        }
                    },
                    {
                        "inputExpression": {
                            "label": "colunaDois",
                            "typeRef": "number"
                        }
                    }
                ],
                "rule": [{
                        "inputEntry": [{
                                "text": "1"
                            },
                            {
                                "text": "1"
                            }
                        ],
                        "outputEntry": {
                            "text": "1"
                        }
                    },
                    {
                        "inputEntry": [{
                                "text": "1"
                            },
                            {
                                "text": "0"
                            }
                        ],
                        "outputEntry": {
                            "text": "1"
                        }
                    },
                    {
                        "inputEntry": [{
                                "text": "0"
                            },
                            {
                                "text": "1"
                            }
                        ],
                        "outputEntry": {
                            "text": "1"
                        }
                    },
                    {
                        "inputEntry": [{
                                "text": "0"
                            },
                            {
                                "text": "0"
                            }
                        ],
                        "outputEntry": {
                            "text": "0"
                        }
                    }
                ]
            }
        }
    }
}
```

### App setup

![image](https://github.com/GiovaniPM/JDMn/assets/9011792/4740bd33-0198-4160-8c18-2ae8f6a37e49)
![image](https://github.com/GiovaniPM/JDMn/assets/9011792/2e4dfa64-12ea-4e15-80b0-d5b34f0867fa)
![image](https://github.com/GiovaniPM/JDMn/assets/9011792/f04a0281-0284-4471-b076-7f115e7c501b)

## Implementation

### App

```python
import JDMn

JDMnDefs = JDMn.getDefinitionsJDMn("or.json")

dados = {}
dados['colunaUm']   = '1'
dados['colunaDois'] = '0'

desconto, prova = JDMn.evaluateJDMn(JDMnDefs, dados, 'S')

print('Return:', desconto)
```

### API

#### Server

```dos
 .\JDMn\api
python JDMnAPI.py
```

![image](https://github.com/GiovaniPM/JDMn/assets/9011792/1a70d3ad-3544-423f-a0b5-bde71b354e31)

#### Postman client

##### GET

```
http://127.0.0.1:8080/jdmn
```

##### Request Headers

```
Content-Type           application/json
```

##### Body

```json
{
    "evaluate": {
        "JDMn": {
            "definitions": {
                "decision": {
                    "decisionTable": {
                        "input": [
                            {
                                "inputExpression": {
                                    "label": "colunaUm",
                                    "typeRef": "number"
                                }
                            },
                            {
                                "inputExpression": {
                                    "label": "colunaDois",
                                    "typeRef": "number"
                                }
                            }
                        ],
                        "rule": [
                            {
                                "inputEntry": [
                                    {
                                        "text": "1"
                                    },
                                    {
                                        "text": "1"
                                    }
                                ],
                                "outputEntry": {
                                    "text": "1"
                                }
                            },
                            {
                                "inputEntry": [
                                    {
                                        "text": "1"
                                    },
                                    {
                                        "text": "0"
                                    }
                                ],
                                "outputEntry": {
                                    "text": "1"
                                }
                            },
                            {
                                "inputEntry": [
                                    {
                                        "text": "0"
                                    },
                                    {
                                        "text": "1"
                                    }
                                ],
                                "outputEntry": {
                                    "text": "1"
                                }
                            },
                            {
                                "inputEntry": [
                                    {
                                        "text": "0"
                                    },
                                    {
                                        "text": "0"
                                    }
                                ],
                                "outputEntry": {
                                    "text": "0"
                                }
                            }
                        ]
                    }
                }
            }
        },
        "condition": {
            "colunaUm": "0",
            "colunaDois": "1"
        }
    }
}
```

![image](https://github.com/GiovaniPM/JDMn/assets/9011792/9ff02bc1-bac3-4658-bae5-6e2a8df061de)
