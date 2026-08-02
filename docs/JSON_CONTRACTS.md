# AutoDoc-Engine JSON Contracts

## Global Rules

## Research Agent

## Script Agent

## Storyboard Agent

## Scene JSON Engine

## Asset Finder Agent

## Image Generator Agent

## Animation Agent

## Voice Agent

## Scene Composer

## Video Renderer

## Caption Generator

## Music Agent

## Motion Graphics Agent

## Thumbnail Agent

## SEO Agent

## Quality Assurance Agent
# Research Agent JSON Contract

## Purpose

Defines communication format for Research Agent.

---

## Input Format

The Research Agent receives a topic request.

Example:

{
  "agent": "research_agent",
  "request": {
    "topic": "History of Artificial Intelligence"
  }
}

---

## Output Format

The Research Agent returns structured research data.

Example:

{
  "agent": "research_agent",
  "result": {
    "title": "History of Artificial Intelligence",
    "summary": "",
    "facts": [],
    "sources": []
  }
}
## Detailed Research Output Schema

```json
{
  "agent": "research_agent",
  "version": "1.0",
  "research": {
    "topic": "",
    "overview": "",
    "key_points": [],
    "timeline": [],
    "important_entities": [],
    "sources": []
  },
  "metadata": {
    "created_at": "",
    "confidence_score": 0
  }
}
## Error Response Format

When the Research Agent fails, it returns:

```json
{
  "agent": "research_agent",
  "status": "error",
  "error": {
    "code": "RESEARCH_FAILED",
    "message": "",
    "details": ""
  }
}



