# Docker Learning Notes

## What is Docker?

Docker is an open-source platform that allows you to build, package, and run applications inside containers.  
A container bundles together everything an application needs — code, runtime, libraries, and dependencies — into a single portable unit. This ensures the application runs the same way across development, testing, and production, regardless of the underlying system.

**In short:** if it runs in Docker, it runs anywhere.

---

## Why Docker is Important

Software development often struggles with the classic *“it works on my machine”* problem. Docker eliminates this by standardising environments. Developers can build once and run anywhere — from laptops to cloud servers.

Docker has become a cornerstone of DevOps because:  
- It accelerates development and deployment cycles.  
- It makes collaboration between teams smoother.  
- It integrates tightly with CI/CD pipelines and modern cloud platforms.  

---

## Key Benefits of Docker

- **Portability** – Applications can run on any OS or cloud platform with Docker installed.  
- **Consistency** – Every environment (dev, test, production) runs the same container image.  
- **Efficiency** – Containers share the host’s OS kernel, making them lighter and faster than virtual machines.  
- **Isolation** – Each container runs independently, reducing conflicts between applications.  
- **Scalability** – Applications can be scaled up/down quickly by running multiple containers.  
- **Ecosystem** – Works seamlessly with orchestration tools (Kubernetes, Swarm) and cloud-native services.  

---

## What I Covered in My Learning

- **Images and Containers** –  
  Images are blueprints (read-only templates), and containers are running instances of those images.  

- **Dockerfiles** –  
  Defined a set of instructions to build custom images automatically instead of manually configuring environments.  

- **Building Images** –  
  Learned how to build images from Dockerfiles, ensuring reproducibility and version control of environments.  

- **Creating a Simple Web App** –  
  Packaged a Flask-based web app inside a Docker container to understand real-world use cases.  

- **Containers and Containerisation** –  
  Explored how containerisation isolates apps while still being resource-efficient compared to full virtual machines.  

- **Docker Compose** –  
  Used `docker-compose.yml` to run multi-container applications (e.g., web app + database + proxy) with a single command.  

- **Docker Networking** –  
  Learned how containers communicate internally via bridges, exposed ports, and how services are linked together.  

- **Docker Registries & Docker Hub** –  
  Pushed and pulled images from Docker Hub, understanding how registries serve as the distribution point for containers in teams and production environments.  

