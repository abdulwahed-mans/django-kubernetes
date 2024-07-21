## Deploying a Django Application to Kubernetes

This guide walks you through setting up a Django project, packaging it as a Docker image, and deploying it to a local Kubernetes environment using Docker Desktop.

**Prerequisites:**

* Docker Desktop (with Kubernetes enabled)
* Python 3.9 or later
* Django 3.2 or later

**Steps:**

1. **Set Up the Project**

   ```bash
   django-admin startproject myproject
   cd myproject
   ```

2. **Create a Dockerfile**

   Create a file named `Dockerfile` in your project directory with the following content:

   ```dockerfile
   # Use the official Python image
   FROM python:3.9

   # Set the working directory
   WORKDIR /app

   # Copy requirements and install dependencies
   COPY requirements.txt requirements.txt
   RUN pip install -r requirements.txt

   # Copy the rest of the project files
   COPY . .

   # Set environment variables for Django
   ENV DJANGO_SETTINGS_MODULE=myproject.settings
   ENV PYTHONUNBUFFERED 1

   # Collect static files
   RUN python manage.py collectstatic --noinput

   # Run the development server
   CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
   ```

3. **Create requirements.txt**

   Ensure you have a `requirements.txt` file with all required packages, including Django:

   ```
   Django
   ```

4. **Build and Push the Docker Image**

   Build the Docker image:

   ```bash
   docker build -t abedulwahed/backend:latest .
   ```

   Push the image to a Docker repository (replace with your own):

   ```bash
   docker push abedulwahed/backend:latest
   ```

5. **Create a Kubernetes YAML File**

   Create a file named `docker-django-kubernetes.yaml` with the following content:

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: django-demo
     namespace: default
   spec:
     replicas: 1
     selector:
       matchLabels:
         service: django
     template:
       metadata:
         labels:
           service: django
       spec:
         containers:
          - name: django-service
            image: abedulwahed/backend:latest
            imagePullPolicy: Always
            env:
             - name: POSTGRES_PASSWORD
               value: mysecretpassword
            ports:
             - containerPort: 8000
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: service-entrypoint
     namespace: default
   spec:
     type: NodePort
     selector:
       service: django
     ports:
     - port: 8000
       targetPort: 8000
       nodePort: 30001
   ```

   **Note:** Replace `mysecretpassword` with your actual password for the PostgreSQL database.

6. **Deploy the Application to Kubernetes**

   Deploy the application:

   ```bash
   kubectl apply -f docker-django-kubernetes.yaml
   ```

7. **Verify the Deployment**

   Verify the deployment:

   ```bash
   kubectl get deployments
   kubectl get services
   ```

8. **Test the Service**

   Test the service using curl:

   ```bash
   curl http://localhost:30001/
   ```

   You should see the Django homepage if everything works correctly.

9. **Remove the Application**

   To remove the application, use the following command:

   ```bash
   kubectl delete -f docker-django-kubernetes.yaml
   ```

This guide provides a step-by-step process to deploy your Django application to a Kubernetes cluster using Docker. Remember to replace placeholders like `mysecretpassword` and image repository name with your own values.
