#!/bin/bash

echo "🌐 Starting Frontend Server..."
echo "================================"

cd frontend

# Check if Python is available
if command -v python3 &> /dev/null; then
    echo "✨ Starting server on http://localhost:3000"
    echo "🎨 Open your browser to http://localhost:3000"
    echo "================================"
    python3 -m http.server 3000
elif command -v python &> /dev/null; then
    echo "✨ Starting server on http://localhost:3000"
    echo "🎨 Open your browser to http://localhost:3000"
    echo "================================"
    python -m http.server 3000
else
    echo "❌ Python not found. Please open index.html directly in your browser."
    echo "📂 File location: $(pwd)/index.html"
fi
