# Domain-Specific Ontology (Text Outline)

## Reused Classes
- :Actor
- :Context
- :ContinuantResource
- :DigitalTwin
- :HumanActor
- :Interpretability
- :NonHumanActor
- :Operational
- :RoutingFlexibility
- :Schedule
- :TaskVariety
- :Technical
- esco:Skill

## Reused Object Properties
- (none)

## Reused Data Properties
- :hasActorRole
- :hasConfidence

## New Class Candidates
- **Manufacturing Pilot** — A specific pilot related to manufacturing processes  (e.g., "# AI4Work-D1.1 (2024) - Pilots Requirements Analysis & Update of SotA")
- **Manufacturing** — The process of making products on a large scale  (e.g., "# AI4Work-D1.1 (2024) - Pilots Requirements Analysis & Update of SotA")
- **Production halts** — Interruptions in the production process.  (e.g., "Consequently, this leads to inconsistent production reliability across different shifts, characterized by more frequent production halts and extended repair times, particularly during night shifts which lack experienced operators (despite the need for continuous operation).")
- **Legal monitoring** — The practice of monitoring activities in compliance with relevant laws and regulations.  (e.g., "Possible methods include recording via cameras, using sensors or wearables, or having operators orally or in writing document their tasks. This involves a crucial challenge: determining how to effectively and legally monitor operator actions.")
- **State of the Art** — A current level of development or attainment, especially in a particular field.  (e.g., "## 3. Update of State of the Art")
- **human representation within an industrial DT** — A digital representation of a human in an industrial digital twin.  (e.g., "The creation of a digital twin of the human being itself aims to create a digital representation of the person, including physical parameters and possibly including a data connection monitoring the physical state of the individual.")
- **human factors** — The uncertainties and variabilities of human behavior.  (e.g., "In the behavioural and decision module, where the scientific challenge resides, to include human factors.")
- **Sliding Work Sharing Mechanisms (SWS)** — A system that allows for the balance between human and machine activities to vary during operation, depending on the situational context, machine-based confidence levels and human interactions  (e.g., "'Sliding work sharing' is defined as an approach where the balance between human and machine activities varies during the operation, depending on the situational context, machine-based confidence levels and human interactions")
- **Adjustable Autonomy** — A system that allows for the level of autonomy to vary during operation, depending on the respective situation  (e.g., "Sliding autonomy, also called 'adjustable autonomy', was researched extensively in the domains of robotics and (multi-)agent systems")
- **Ten Levels of Automation** — A set of ten levels that can be used to differentiate potential levels of autonomy  (e.g., "A variety of potential levels of autonomy may be differentiated, e.g. considering the ten levels of automation suggested in")
- **Pilot Specific SotA** — A specific state-of-the-art pilot review  (e.g., "## 4. Pilot Specific SotA review")
- **OEE** — Overall equipment effectiveness as a measure of efficiency for the manufacturing industry  (e.g., "In 2021, the European Committee for Standardization released the European Standard EN 415-11, which standardized the overall equipment effectiveness (OEE)...")
- **SWS Management** — A system that facilitates dynamic sharing of work between humans and AI/robots.  (e.g., "# AI4Work-D1.2 (2024) - AI4Work Concept")
- **SWS** — A short form for Sliding Work Sharing.  (e.g., "The SWS Management component aims to facilitate dynamic sharing of work between humans and AI/robots.")
- **Sliding Work Sharing** — A system that dynamically adjusts the level of human/machine involvement based on work situation and uncertainty.  (e.g., "The SWS Management component aims to facilitate dynamic sharing of work between humans and AI/robots.")
- **decision** — The outcome of considering the required degree of involvement of the human and the (degree of) support to be provided to the human.  (e.g., "Depending on the respective work situation, the SWS Management shall decide about the required degree of involvement of the human, considering the current level of uncertainty of the AI/robot.")
- **unusual situation** — A work situation that is not common or typical.  (e.g., "In case of high uncertainty of the AI in an unusual situation, the decision may fall to the human (see Figure 14).")
- **common situation** — A work situation that is typical or frequent.  (e.g., "In case of low uncertainty of the AI in a common situation, the decision/action may be suggested by the AI and confirmed by the human (see Figure 15).")
- **very common situation** — A work situation that is extremely typical or frequent.  (e.g., "In case of very low uncertainty of the AI in a very common situation, the decision may be automatically made by the AI, with human intervention possible but optional (see Figure 16).")
- **Sliding Work Sharing Management** — A component that decides the appropriate degree of human involvement and support to the human depending on the work situation.  (e.g., "The SWS Management component aims to take these different inputs into account when deciding about the appropriate degree of human involvement – and/or the degree of support to the human – depending on the respective work situation.")
- **Sliding Work Sharing approach** — A work-sharing approach where the balance between human and machine activities varies during the operation, depending on the situational context, machine-based confidence levels and human interactions.  (e.g., "SWS is defined as a work-sharing approach where the balance between human and machine (AI or robot) activities varies during the operation, depending on the situational context, machine-based confidence levels and human interactions")
- **AI4Work technology** — Technology used in AI4Work systems  (e.g., "The workflow may be initiated by a human, a robot, some AI4Work technology (e.g. a Digital Twin that monitors the processes, ...)")
- **pilot-specific AI components** — AI components specific to a pilot or use case that provide input data to the SWS Management component  (e.g., "The workflow needs to be defined in advance and is kept in the “workflow definition storage”. At runtime, the “workflow executor” reads this workflow definition and orchestrates the work: ... It triggers other systems/components and requests input data.")
- **Sliding Work Sharing** — A system that decides the degree of human involvement in a work situation based on AI uncertainty and user preferences.  (e.g., "The SWS Management shall decide about the degree of human involvement that is required in the respective work situation, depending on the uncertainty of the AI.")
- **Evaluation Approach** — A method or set of methods used to assess the quality, performance, or effectiveness of a system or product.  (e.g., "## 5. Evaluation Approach and Laboratory Prototypes")
- **ONTOLOGY** — A formal naming system used for representing a domain of interest.  (e.g., "The ONTOLOGY terms that appear in the dictionary should be used for 'ontology_term'.")
- **concept** — An abstract idea or notion that is general and not associated with a specific instance.  (e.g., "Mapped concepts should have an 'ontology_term' assigned.")
- **Adaptive training modules** — Training materials tailored to an individual's skill level or learning style.  (e.g., "The Training system incorporates the following technologies to achieve its goals: • Data Collection and Handling for AI/Robotics Services: Centralizes training data from operator manuals and real-time machine usage to create adaptive training modules.")

## New Object Property Candidates
- **Monitor operator actions** — The act of observing or recording an operator's actions during work.  (e.g., "Possible methods include recording via cameras, using sensors or wearables, or having operators orally or in writing document their tasks.")
- **mapping** — The process of associating one thing with another.  (e.g., "Mapped concepts should have an 'ontology_term' assigned.")

## New Data Property Candidates
- **Repair times** — The duration of time required to repair equipment or machinery.  (e.g., "Consequently, this leads to inconsistent production reliability across different shifts, characterized by more frequent production halts and extended repair times, particularly during night shifts which lack experienced operators (despite the need for continuous operation).")
- **adequate data model** — A suitable data structure for representing workers and their interactions with other assets of the system in a digital twin.  (e.g., "The main additions are in the data persistence module where an adequate data model needs to be integrated for the representation of the workers and their interactions with other assets of the system.")
- **pilot/use-case-specific rules** — Rules specific to a pilot or use case that are stored in the Sliding module's rule storage  (e.g., "At runtime the “decision engine” applies these rules to the current input data (which is received from other AI4Work components and pilot-specific AI components) in order to dynamically decide about the recommended degree of AI autonomy and/or support to the human in the current situation.")
- **text** — A sequence of words or sentences forming a coherent and meaningful unit of language.  (e.g., "The text should be analyzed to identify concepts and their relationships.")
- **ai_confidence** — A variable representing the confidence level of an AI system.  (e.g., "IF ai_confidence IS low THEN suggested_work_sharing_approach IS human_manually;")

## Unspecified-Type Candidates