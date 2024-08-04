Django recreation of GrixusVisionBackend, which is made in fastAPI. This purpose of building this was to learn Django. And also, more devops / deployment reps never hurt.

So far I have deployed all my projects on a DigitalOcean Ubuntu droplet. This github action shown here is the only kind I have ever built, which just SSH's into the server and updates (stop service, git pull, start service) on branch push.
