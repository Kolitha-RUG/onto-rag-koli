# Domain-Specific Ontology (Text Outline)

## Reused Classes
- :AIAcceptance
- :Actor
- :Context
- :Decision
- :DigitalTwin
- :HumanActor
- :NonHumanActor
- :Operational
- :Status
- :Task
- esco:Skill
- sosa1:Sensor

## Reused Object Properties
- (none)

## Reused Data Properties
- :hasActorRole
- :hasConfidence

## New Class Candidates
- **Manufacturing** — A specific type of industry or production process involving the creation of goods using machinery, tools, chemical materials, and/or labor.  (e.g., "# AI4Work-D1.1 (2024) - Pilots Requirements Analysis & Update of SotA")
- **Pilots** — A test or trial run of a system, product, or service to evaluate its performance and effectiveness.  (e.g., "# AI4Work-D1.1 (2024) - Pilots Requirements Analysis & Update of SotA")
- **Operational Equipment Effectiveness** — A measure of the productivity and efficiency of equipment in a production process.  (e.g., "Packaging material production lines are generally highly automated yet susceptible to multiple minor disruptions, which significantly impact Operational Equipment Effectiveness (OEE).")
- **production reliability** — The ability of a production process to consistently produce goods without significant disruptions.  (e.g., "Consequently, this leads to inconsistent production reliability across different shifts, characterized by more frequent production halts and extended repair times, particularly during night shifts which lack experienced operators (despite the need for continuous operation).")
- **knowledge gaps** — The difference between what operators know and what they need to know to effectively perform their tasks.  (e.g., "The manufacturing pilot aims to address this issue with an AI-powered digital production assistant designed to bridge the knowledge gaps among operators and between operators and machines.")
- **operator actions** — The tasks and behaviors performed by operators in a manufacturing process.  (e.g., "Capturing knowledge from experienced workers by documenting maintenance and repair operations involves a crucial challenge: determining how to effectively and legally monitor operator actions.")
- **maintenance and repair operations** — The tasks performed to maintain or repair equipment in a manufacturing process.  (e.g., "Capturing knowledge from experienced workers by documenting maintenance and repair operations involves a crucial challenge: determining how to effectively and legally monitor operator actions.")
- **State of the Art** — A current level or stage in a particular field, especially one that is considered to be the best or most advanced.  (e.g., "## 3. Update of State of the Art")
- **Human-Cyber-Physical-Systems** — A system that combines human, cyber, and physical elements to achieve human-automation symbiosis work systems.  (e.g., "The operator 4.0 works aided by machines and if needed by means of Human-Cyber-Physical-Systems.")
- **advanced human-machine interaction technologies** — Technologies that enable smart and skilled operators to work cooperatively with robots and machines.  (e.g., "The operator 4.0 works aided by advanced human-machine interaction technologies.")
- **adaptive automation** — Automation that adjusts its behavior based on the fatigue level of the worker monitored using real-time sensor data.  (e.g., "The support given from a collaborative robot to the human operator was adjusted on the basis of the fatigue level of the worker.")
- **Sliding Work Sharing Mechanisms (SWS)** — A system that aims to find the ideal balance between human and machine activities depending on the respective situation  (e.g., "'Sliding work sharing' is defined as an approach where the balance between human and machine activities varies during the operation, depending on the situational context, machine-based confidence levels and human interactions")
- **Adjustable Autonomy** — A concept researched extensively in robotics and multi-agent systems that allows varying the level of autonomy during operation, depending on the respective situation  (e.g., "Sliding autonomy, also called 'adjustable autonomy', was researched extensively in the domains of robotics and (multi-)agent systems")
- **Ten Levels of Automation** — A suggested set of ten levels of automation for robots and AI systems  (e.g., "A variety of potential levels of autonomy may be differentiated, e.g. considering the ten levels of automation suggested in")
- **Pilot Specific SotA** — A specific state-of-the-art related to a pilot program or project  (e.g., "## 4. Pilot Specific SotA review")
- **IMA E-CO Flex** — A specific type of machine.  (e.g., "1. AI4WORK shall provide a troubleshooting tool that utilizes the IMA E-CO Flex machine’s current status and fault data, in conjunction with historical fault records and machine learning models, to accurately diagnose issues and recommend appropriate solutions.")
- **Sliding Work Sharing Management** — A component that facilitates dynamic sharing of work between humans and AI/robots.  (e.g., "# AI4Work-D1.2 (2024) - AI4Work Concept")
- **SWS situation** — A specific work situation in the context of Sliding Work Sharing.  (e.g., "In case of high uncertainty of the AI in an unusual situation, the decision may fall to the human (see Figure 14).")
- **Sliding Work Sharing (SWS)** — A work-sharing approach where the balance between human and machine activities varies during the operation, depending on the situational context, machine-based confidence levels and human interactions.  (e.g., "The SWS Management component aims to take these different inputs into account when deciding about the appropriate degree of human involvement – and/or the degree of support to the human – depending on the respective work situation.")
- **work situation** — A specific context or scenario in which work is being performed  (e.g., "The Context Awareness component extracts the contextual information about the current work situation")
- **decision/action** — An outcome or result of a process that requires a choice or action  (e.g., "The AI/robot suggests a decision/action based on the context information")
- **legacy system** — An existing system that can adapt its behavior based on the decision/recommendation of the SWS Management component  (e.g., "An existing (legacy) system, which can adapt its behaviour based on the decision/recommendation of the SWS Management component.")
- **sliding autonomy** — A concept that refers to the ability of an AI system to dynamically adjust its level of control in a task, working collaboratively with humans.  (e.g., "Application of the concepts of “sliding autonomy” [28], [29], [30] and “sliding decision making” [31] to the domain of “work sharing between human and AI”.")
- **sliding decision making** — A decision-making approach that allows an AI system to dynamically adjust its level of control in a task, working collaboratively with humans.  (e.g., "Application of the concepts of “sliding autonomy” [28], [29], [30] and “sliding decision making” [31] to the domain of “work sharing between human and AI”.")
- **Evaluation Approach** — A method or set of methods used to assess the quality, performance, or effectiveness of a system or product.  (e.g., "## 5. Evaluation Approach and Laboratory Prototypes")
- **Laboratory Prototypes** — A preliminary version of a system or product that is tested and evaluated in a controlled environment.  (e.g., "## 5. Evaluation Approach and Laboratory Prototypes")
- **Ontology** — a set of concepts within a domain and the relationships between those concepts  (e.g., "ONTOLOGY")
- **OWL Class** — a class in the OWL ontology language  (e.g., "http://www.w3.org/2002/07/owl#Class")
- **SWS** — A system or component that dynamically decides about the degree of AI autonomy vs. the degree of human involvement.  (e.g., "The aim of the laboratory prototype for the SWS Management component was to do early experiments regarding the core functionality of the SWS, i.e. the sliding module that shall dynamically decide about the degree of AI autonomy vs. the degree of human involvement.")
- **sliding work sharing** — A method or approach for dynamically deciding about the degree of AI autonomy vs. the degree of human involvement.  (e.g., "The aim of the laboratory prototype for the SWS Management component was to do early experiments regarding the core functionality of the SWS, i.e. the sliding module that shall dynamically decide about the degree of AI autonomy vs. the degree of human involvement.")
- **MaintenanceTicket** — A document created when a fault occurs in an automated packing machine that exceeds the expertise of the maintenance operator.  (e.g., "When a fault occurs in an E-CO Flex machine that exceeds the expertise of the maintenance operator, a maintenance ticket is created.")
- **Training system instance** — A system designed to train operators on the use of complex machinery.  (e.g., "The Training system incorporates the following technologies to achieve its goals:")
- **E-CO Flex machine** — A type of packaging machine used in the AI4Work project.  (e.g., "The Early Prototype aims to schedule the replenishment of a packaging line, which includes one E-CO Flex machine, N packaging operators (with N ≥ 2) and one replenishment operator.")
- **N packaging operators** — A group of operators working within a packaging line in the AI4Work project.  (e.g., "The Early Prototype aims to schedule the replenishment of a packaging line, which includes one E-CO Flex machine, N packaging operators (with N ≥ 2) and one replenishment operator.")

## New Object Property Candidates
- **OWL Object Property** — an object property in the OWL ontology language  (e.g., "http://www.w3.org/2002/07/owl#ObjectProperty")

## New Data Property Candidates
- **mean time to repair** — The average time it takes to repair a piece of equipment in a manufacturing process.  (e.g., "Linking specific maintenance and repair operations to different types of failures, assessing and ranking their effectiveness based on metrics such as mean time to repair and possibly the time until a similar or related failure occurs again.")
- **pilot/use-case-specific rules** — Rules defined for a specific pilot or use case that are used by the Sliding module  (e.g., "At runtime the “decision engine” applies these rules to the current input data ...")
- **OWL Datatype Property** — a datatype property in the OWL ontology language  (e.g., "http://www.w3.org/2002/07/owl#DatatypeProperty")
- **OperatingManual** — A collection of instructions for operating and maintaining automated packing equipment.  (e.g., "Operators, aiming to improve their skills in machine operations and maintenance, access a virtual assistant. This assistant uses natural language processing to extract information from operating manuals and offers step-by-step guidance tailored to the operator’s skill level.")

## Unspecified-Type Candidates
- **QName** — a string consisting of a local part and a namespace prefix, used to uniquely identify elements in XML namespaces  (e.g., "<qname or iri>")
- **IRI** — Internationalized Resource Identifier, a string that can contain international characters and is used to identify resources on the web  (e.g., "<qname or iri>")