## Backend Software Engineer Test: Containerized Task Management with Docker API

The primary goal of this project is to assess the applicant's proficiency in backend development, especially in the context of containerization using Docker. The candidate will be evaluated on their ability to design and implement a robust backend system, integrate with Docker's Engine API, and collaborate effectively with other developers.

The test involves creating a containerized task management system where tasks are executed within Docker containers. The candidate's contributions will be evaluated based on the completion of specified tasks, and successful candidates will be invited for an interview with the team.

## How does this work ?

Candidates will concurrently work on a set of tasks related to the project. Once a candidate deems their contribution complete, they can submit a pull request. The team will review the contribution, provide feedback, and merge the changes if satisfactory. Completed tasks will be omitted, and new tasks will be assigned to other candidates. Candidates with merged changes will be invited for an interview with the team.


## Who can apply ?

This test is open to both students seeking an internship at BIGmama and professionals looking for a full-time position.


## Tasks

#### 1. Containerized Task Execution:
   - Design an API within the package to seamlessly create, manage, and execute tasks within Docker containers.
   - Utilize Docker Engine API to ensure tasks are containerized effectively.
   - Implement robust error handling and logging for containerized task execution.

#### 2. Task Dependencies and Scheduling:
   - Extend the system to handle task dependencies, allowing users to define the order of task execution.
   - Implement a scheduling mechanism for recurring tasks, providing flexibility for various use cases.

#### 3. Plugin System for Extensibility:
   - Develop a plugin system that empowers users to extend the functionality of the task management system.
   - Plugins should encapsulate specific features, allowing for easy integration of custom execution types, notifications, or storage options.

#### 4. Real-time Monitoring and Notifications:
   - Implement real-time monitoring of task execution within containers.
   - Provide notification features to alert users about the status of their tasks.

#### 5. Security Measures:
   - Ensure the security of the system by implementing appropriate measures for user authentication and authorization.
   - Incorporate secure communication practices for API endpoints.

#### 6. Unit and Integration Testing:
   - Develop comprehensive unit tests to validate the functionality of different components.
   - Include integration tests to ensure seamless interactions between various system modules.

#### 7. Documentation and Examples:
   - Provide clear and comprehensive documentation for setting up, configuring, and running the backend system.
   - Include example code snippets and use cases to guide users in different scenarios, such as task automation and integration with existing applications.

#### 8. Performance Optimization:
   - Optimize the performance of the system to handle a large number of concurrent tasks.
   - Implement caching strategies and other optimizations to enhance overall responsiveness.


## Setup

Clone the repository
```bash
git clone git@github.com:BIGmama-technology/Hiring-software-engineer-backend.git 
```


## Contribution guidelines

- Write useful comments to help others understand what you do.
- Commit often and write meaningful commit messages.
- Create a new branch with your name, push your code to it and create a pull request once you finish your contribution.


## Resources
Explore the Docker documentation and relevant API resources to ensure seamless integration:

- [Docker Engine API Documentation](https://docs.docker.com/engine/api/)
- [Docker API Client Libraries](https://docs.docker.com/engine/api/sdk/)


## FAQ

#### What type of tasks can be run ?

- **Script Execution:** Execute custom scripts or commands within the Docker container. This could include running shell scripts, Python scripts, or any other executable code.

- **Application Processes:** Run and manage specific applications or processes within the container. For example, a task could involve starting a web server, running a database process, or executing a background service.

- **Data Processing:** Perform data processing tasks within the container. This might involve tasks like data transformation, analysis, or other computational processes.

- **Scheduled Jobs:** Run tasks on a scheduled basis. For instance, a task could be scheduled to run daily, weekly, or at specific intervals to perform recurring operations.

- **Automation Workflows:** Implement automation workflows within the container. Tasks could be designed to automate various processes, making use of different tools or services.

- **Build and Deployment Processes:** Use containers to facilitate build and deployment processes. Tasks might involve building and packaging applications, deploying them to specific environments, or managing versioning.

- **Testing and Quality Assurance:** Run automated tests within the container to ensure the quality of code or applications. This could include unit tests, integration tests, or end-to-end tests.

- **Background Jobs:** Execute background jobs or asynchronous tasks within the container. This is useful for handling tasks that don't need to run in real-time and can be processed in the background.

- **Task Dependencies:** Create tasks that have dependencies on other tasks. Ensure that the system can manage the order of execution and handle task dependencies effectively.

- **Custom Workflows:** Allow users to define custom workflows by chaining multiple tasks together. This could involve designing a flexible and configurable system for defining and executing complex workflows.


#### how many features should I work on ?
doesn't matter, what important is the value of your contribution and it's quality, impress us !

#### what if the task I am working on gets completed by someone else ?
pick another task, and hurry up !

#### what if I have a question ?
open an issue and we will answer it as soon as possible !

May your coding journey be smooth, and success follows you, Inshallah!