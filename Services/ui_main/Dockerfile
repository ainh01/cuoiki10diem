# Use a lightweight Node.js 18 image as the base
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and yarn.lock first to leverage Docker cache
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the application code
COPY . .

# --- ADD THIS LINE ---
# This generates the .nuxt folder specifically for the container environment
RUN npx nuxi prepare
# ---------------------

# Expose port 3000
EXPOSE 3000

# Start the application
CMD ["yarn", "dev"]
