# AutoDoc-Engine Architecture

## Overview

AutoDoc-Engine is an autonomous AI video production system that converts a topic into a professional documentary video.

## System Layers

### 1. Agent Layer

Contains specialized AI agents:

- Research Agent
- Script Agent
- Storyboard Agent
- Asset Agent
- Voice Agent
- Quality Assurance Agent

### 2. Processing Layer

Handles:

- Data processing
- Scene generation
- Video composition
- Rendering pipeline

### 3. Communication Layer

All agents communicate through defined JSON contracts.

### 4. Output Layer

Produces:

- Documentary video
- Captions
- Audio
- Thumbnail
- SEO metadata

## Development Principle

Each module must be:

- Independently testable
- JSON contract based
- Version controlled
- Verified through GitHub Actions
