import { defineEventHandler } from 'h3'

// Simple health endpoint mounted at GET /health
export default defineEventHandler(() => {
  return {
    status: 'ok',
    uptime: process.uptime(),
    timestamp: Date.now(),
  }
})
