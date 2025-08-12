# Domain-Specific Ontology (Text Outline)

## Reused Classes
- :AIAcceptance
- :Actor
- :ConfidenceAssessment
- :Context
- :DigitalTwin
- :HumanActor
- :Operational
- :Safety
- :Status
- :Task

## Reused Object Properties
- :hasPerformanceDimension

## Reused Data Properties
- :hasConfidence

## New Class Candidates
- **Manufacturing** — A type of industry or production process that involves the physical creation of goods.  (e.g., "# AI4Work-D1.1 (2024) - Pilots Requirements Analysis & Update of SotA")
- **Pilots** — A test or trial of a system, product, or service in real-world conditions.  (e.g., "# AI4Work-D1.1 (2024) - Pilots Requirements Analysis & Update of SotA")
- **Operational Equipment Effectiveness (OEE) Assessment** — A method for evaluating the performance of production equipment.  (e.g., "The AI-powered digital production assistant will link specific maintenance and repair operations to different types of failures, assessing and ranking their effectiveness based on metrics such as mean time to repair and possibly the time until a similar or related failure occurs again.")
- **Legal Monitoring Method** — A method for monitoring operator actions while complying with privacy and labor laws.  (e.g., "Determining how to effectively and legally monitor operator actions is a crucial challenge in capturing knowledge from experienced workers.")
- **Operator Skill Level Assessment** — A method for evaluating an operator's proficiency and experience level.  (e.g., "The AI-powered digital production assistant will provide targeted instructions to operators, tailored to their varying levels of experience to maximize productivity on the line.")
- **State of the Art** — A current level or stage in a particular area of study, technology, or practice.  (e.g., ""3. Update of State of the Art"")
- **Human-Cyber-Physical-Systems** — A system that includes advanced human-machine interaction technologies and adaptive automation towards achieving human-automation symbiosis work systems.  (e.g., "The operator 4.0 works aided by machines and if needed by means of Human-Cyber-Physical-Systems.")
- **Sliding Autonomy Mechanisms (SAM)** — A system that allows for varying the level of autonomy during operation, depending on the respective situation.  (e.g., "In most of the AI4Work pilots, the work sharing will be between human and AI, while only few use cases will deal with work sharing between human and robot. Therefore, when considering the state of the art regarding sliding autonomy of robots in the upcoming development of SAM mechanisms, a basic difference between robots and AI must be considered: a human can rather easily see that a physical robot requires help or could become a safety hazard, but this may not be as easy or even impossible for a human working together with and observing an AI.")
- **Pilot Specific SotA** — A specific state-of-the-art review related to a pilot  (e.g., "## 4. Pilot Specific SotA review")
- **IMA E-CO Flex** — A specific type of packaging/boxing plant hardware used in the scenario.  (e.g., "The context of the described scenario involves an e-commerce packaging/boxing plant populated with several IMA E-CO Flex machines...")
- **Troubleshooting Tool** — A system that suggests solutions based on current faults and historical data.  (e.g., "Provide a troubleshooting tool able to suggest solutions based on current faults and historical data")
- **IMA E-CO Flex** — A specific type of machine  (e.g., "1. AI4WORK shall provide a troubleshooting tool that utilizes the IMA E-CO Flex machine’s current status and fault data, in conjunction with historical fault records and machine learning models, to accurately diagnose issues and recommend appropriate solutions.")
- **AI4WORK solution** — An intelligent system designed to schedule the production line under specific conditions.  (e.g., "The AI4WORK solution is designed to intelligently schedule the production line under these conditions, ensuring a balanced workload between human operators and machines.")
- **sliding work sharing** — A method for dynamically adjusting the distribution of tasks between human operators and machines in real-time.  (e.g., "Technologies: Sliding Work Sharing.")
- **Sliding Work Sharing Management** — A system that facilitates dynamic sharing of work between humans and AI/robots.  (e.g., "# AI4Work-D1.2 (2024) - AI4Work Concept")
- **SWS situation** — A specific work scenario involving humans and AI/robots under Sliding Work Sharing.  (e.g., "In case of high uncertainty of the AI in an unusual situation, the decision may fall to the human (see Figure 14).")
- **Sliding Work Sharing (SWS)** — A work-sharing approach where the balance between human and machine activities varies during the operation, depending on the situational context, machine-based confidence levels and human interactions.  (e.g., "The SWS Management component aims to take these different inputs into account when deciding about the appropriate degree of human involvement – and/or the degree of support to the human – depending on the respective work situation.")
- **SWS Management component** — A system that decides or recommends the degree of AI autonomy and/or support to a human in response to events/situations at plan execution time.  (e.g., "The SWS Management component then “decides” or “recommends” to what extent the AI/robot may work autonomously and if the actions/decision should be requested from (or checked/confirmed by) the human operator.")
- **Sliding Work Sharing** — A system that decides about the degree of human involvement in a work situation based on AI uncertainty and user preferences.  (e.g., "The SWS Management component shall decide about the degree of human involvement that is required in the respective work situation, depending on the uncertainty of the AI.")
- **Evaluation Approach** — A method or set of methods used to assess the performance, quality, or effectiveness of a system or product.  (e.g., "## 5. Evaluation Approach and Laboratory Prototypes")
- **Laboratory Prototypes** — A preliminary version of a system or product that is tested and evaluated in a controlled environment.  (e.g., "## 5. Evaluation Approach and Laboratory Prototypes")
- **Formal Ontology Representation** — A method or system for representing concepts and relationships in a formal ontology.  (e.g., "ONTOLOGY terms are used to represent concepts and relationships in a formal ontology.")
- **SWS** — A system or component that dynamically decides about the degree of AI autonomy vs. the degree of human involvement.  (e.g., "The aim of the laboratory prototype for the SWS Management component was to do early experiments regarding the core functionality of the SWS, i.e. the sliding module that shall dynamically decide about the degree of AI autonomy vs. the degree of human involvement.")
- **SWS Management** — A system or component that manages work sharing.  (e.g., "Figure 39: Visualization of the SWS Management Lab Prototype")
- **fuzzy sets low/medium/high** — A set of values with a degree of membership defined by a membership function.  (e.g., "FUZZIFY human_experience_level TERM low := (0, 1) (2, 1) (4,0);")
- **Training system** — A system designed for training operators on complex machinery.  (e.g., "The Training system incorporates the following technologies to achieve its goals:")

## New Object Property Candidates
- **decentralized computational decision-making process** — A process that allows humans to take part in a decision-making process using HDTs.  (e.g., "HDTs are proposed to collect and communicate workers’ skills, preferences, personality and to enable humans to take part to a decentralized computational decision-making process which leads to an improved scheduling.")
- **AI Interpretation** — The ability of AI to interpret failures/inefficiencies and formulate responses based on historical data.  (e.g., "AI interprets the failure and gives troubleshooting support.")
- **plan’s validation** — The process of checking the results of a plan to ensure its correctness and suitability for execution.  (e.g., "Make the decision about the need for re-planning/re-scheduling in case of an unexpected situation at “plan execution time”")
- **re-calculation of the work plan** — The process of re-evaluating and adjusting the original work plan in response to major disruptions.  (e.g., "In such a case it will trigger other AI4Work components to do a re-planning.")
- **sliding rules** — Configurable rules that customize Sliding Work Sharing to different pilot use cases.  (e.g., "Shall: Support customization to different pilot use cases via configurable “sliding rules”.")
- **workflow definitions** — Configurable structures that outline the steps and interactions between components in a workflow.  (e.g., "May: Facilitate customization to different pilot use cases via “configurable workflow definitions”.")
- **fuzzy rules** — A conditional statement that determines the output of a fuzzy system based on the input and membership functions.  (e.g., "IF ai_confidence IS low THEN suggested_work_sharing_approach IS human_manually;")
- **de-fuzzification** — The process of converting the output of a fuzzy system, which is a set of membership degrees, into a single numerical value.  (e.g., "The application of all applicable fuzzy rules and the subsequent “de-fuzzification” results in a numerical value for the “suggested work sharing approach” (in this example it starts from “human doing the work manually” via “human in/on the loop” up to the “AI working autonomously”).")

## New Data Property Candidates
- **Machine State** — The current state of a machine as observed or recorded.  (e.g., "An E-CO Flex machine encounters a fault beyond the expertise of the maintenance operator. The machine operator contacts maintenance assistance, opening a ticket that provides information about the current state of the machine and, eventually, other useful information like production data and sensor readings.")
- **one-size-fits-all** — A solution that is designed to work for all users or situations without needing to be adapted.  (e.g., "the SWS Management will not be one monolithic component with a “one-size-fits-all” approach, but will rather provide generic reusable framework elements")
- **pilot/use-case-specific rules** — Rules that must be defined in advance for the SWS Management component's decision engine.  (e.g., "At runtime the “decision engine” applies these rules to the current input data (which is received from other AI4Work components and pilot-specific AI components) in order to dynamically decide about the recommended degree of AI autonomy and/or support to the human in the current situation.")
- **AI autonomy level** — The degree of automation or control that an AI system has, as determined by user preferences and/or company guidelines.  (e.g., "Shall: Take into account the user preferences and/or company guidelines regarding the AI autonomy level (e.g. some users may want to always double-check AI decisions, other users may trust the AI to work in automatic mode, some company may want to assure that there is always a human in the loop).")
- **N** — A variable representing the number of packaging operators or packaging bays.  (e.g., "The Early Prototype aims to schedule the replenishment of a packaging line, which includes one E-CO Flex machine, N packaging operators (with N ≥ 2) and one replenishment operator.")

## Unspecified-Type Candidates