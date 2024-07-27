# ContentCreatorsAgency
## Overview
ContentCreatorsAgency is an innovative project designed to streamline the content creation process from strategy to final approval, ensuring high-quality, engaging content that meets client expectations. Our agency workflow and structure ensure cohesive and effective content to promote sustainable practices in urban environments.

## Manifesto
### Mission
To streamline the content creation process from strategy to final approval, ensuring high-quality, engaging content that meets client expectations.

### Goals
1. Establish clear content strategies that align with client objectives.
2. Create well-structured and engaging drafts.
3. Ensure thorough editing for coherence and style.
4. Maintain clear communication with clients throughout the process.

### Project Structure
The project is organized as follows:

`agents.py`: Main script to run the agency operations.
`requirements.txt`: Contains all the dependencies needed for the project.
`agency_manifesto.md`: Shared instructions and manifesto for all agents.

## Installation
To set up the project, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/Apurv-Salunke/agency-swarm-projects.git
    cd ContentCreatorsAgency
    ```
2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```
3. Create a .env file in the project root directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```
### Usage
To run the project, use the following command:
```sh
python3 agents.py
```
### Workflow

* Content Strategist (CEO): Defines the topic, objectives, and key points to create a clear outline.
Communicates with the Content Writer, Editor, and Client Relations Manager.
* Content Writer:Drafts a cohesive, conversational piece based on the outline provided by the CEO.
Refines content based on the Editor's feedback.
Generates multiple versions using different prompts.
* Editor:
Reviews the draft for structure, flow, and style consistency.
Performs redundancy checks and ensures style uniformity.
Combines the best elements from multiple versions to create a high-quality final draft.
* Client Relations Manager:Acts as the sole point of contact with the client. Submits the final draft for approval and incorporates any necessary revisions.

## Scope for Improvement
While the current implementation of ContentCreatorsAgency provides a solid foundation for managing the content creation process using AI agents, there is significant potential for future enhancements. Some areas for improvement include:

* Integrating external tools and APIs to enhance functionality and efficiency.
* Implementing better prompting or fine-tuning for better content generation and editing.
* Adding automated performance analysis and feedback loops to continuously improve content quality.
* Expanding the roles and capabilities of AI agents to handle more complex tasks and workflows.

## Contributions
We welcome contributions to enhance the project. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request and describe your changes.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or feedback, please reach out to us [here](salunke.apurv7@gmail.com).

