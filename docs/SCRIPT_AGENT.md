# Script Agent

## Overview

The Script Agent converts structured research data into a professional documentary script.

## Purpose

The Script Agent is responsible for transforming research information into a storytelling format suitable for video production.

## Responsibilities

- Generate documentary narration
- Create engaging hooks
- Structure video sections
- Maintain storytelling flow
- Convert facts into audience-friendly explanations

## Input

The Script Agent receives research data from the Research Agent.

Input example:

```json
{
  "agent": "research_agent",
  "research": {
    "topic": "History of Artificial Intelligence",
    "facts": []
  }
}
## Workflow

The Script Agent works in the following pipeline:

Research Agent
        ↓
Script Agent
        ↓
Storyboard Agent
## Processing Flow

1. Receive research data from Research Agent
2. Analyze important facts
3. Create documentary structure
4. Generate narration script
5. Prepare output for Storyboard Agent
## Script Structure

A generated script contains:

- Title
- Hook
- Introduction
- Main Sections
- Narration
- Ending / Conclusion

## Status

Architecture Design Completed
