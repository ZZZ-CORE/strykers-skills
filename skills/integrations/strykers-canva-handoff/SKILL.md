---
name: strykers-canva-handoff
description: After an Empire Strykers graphic is made, offers three ways to continue in Canva (finished PNG, editable PPTX, or reusable team template), prepares the chosen file, and gives import steps. Use when a graphic is done and the user may want to edit or reuse it in Canva.
---

# Strykers Canva Export & Handoff

> New draft skill (October 2026), written from skill 09 in `strykers-creative-studio-gpt/docs/24-SKILL-LIBRARY.md`. Not yet tested in production; check the output before relying on it.

Get finished graphics into Canva in the form the user needs.

## When to use

- Right after generating or finishing a graphic.

## Steps

1. Run a brand check first (see the `strykers-brand-qa` skill). Don't hand off a BLOCKED asset.
2. Offer three options:
   1. **Finished PNG:** one flat image, ready to upload to Canva and post.
   2. **Editable PPTX:** text, shapes, and images as separate pieces where possible, for importing into Canva and editing.
   3. **Reusable team template:** a layout with placeholders the team can copy for future posts.
3. Prepare the chosen format.
4. Hand off:
   - **If a Canva connection is available**, use it and report only what the tool confirms (for example, a returned design link or ID).
   - **If not**, give manual steps:
     - PNG: in Canva, open **Uploads**, upload the file, and add it to a design.
     - PPTX: in Canva, upload or import the PowerPoint file; check fonts and layout after import.
     - Template: create the design in Canva, then share it with the team or save it as a template if the team's Canva plan supports that.

## Rules

- Don't promise that every layer will stay editable after a PPTX import; flattened images and unsupported fonts may not.
- Don't say a file is in Canva unless a connected tool confirmed it.
- Brand fonts may need to be uploaded to Canva by the team (license permitting).

## Output

- The file in the chosen format.
- Import instructions.
- Connection status: "Sent to Canva (link)" only with tool confirmation; otherwise "Not sent; manual upload steps above".

## Before you finish

- The brand check was done before handoff.
- No direct Canva transfer or full editability is claimed without evidence.
