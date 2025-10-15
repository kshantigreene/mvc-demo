# To-Do List App — MVP Specifications

## 1) Functional Specifications

**F1. Add Task**
User enters text and presses Enter or clicks Add. Task appears at top of Active list. Text is trimmed and space-collapsed. Reject if empty or exceeds 100 characters. Reject duplicates (case-insensitive) with message "Task already exists."

**F2. View Tasks**
Two sections: Active (unchecked tasks) and Completed (read-only). Both show newest first. Display "No active tasks" or "No completed tasks" when empty.

**F3. Complete Task**
Click checkbox to move task from Active to Completed. Update persists immediately.

**F4. Persist Data**
Save to `todo.json` after every change. Load on startup. If file missing or corrupted, create backup and start fresh.

---

## 2) Interface Specifications

**Layout**
- Title bar: "To-Do List"
- Active section with checkboxes
- Input field with "Add" button
- Completed section (bullets, no interaction)
- Minimum window: 480×360px

**User Actions**
- Type task and press Enter or click Add
- Click checkbox to complete task
- Tab navigation through all controls
- Hover highlights active tasks

**Feedback**
- Tasks appear/move instantly (<100ms)
- Validation messages show below input field
- Empty states use muted text

---

## 3) Performance Requirements

- Startup: render in ≤300ms with 300 tasks
- Add/complete: update UI in ≤100ms
- File writes: async, complete in ≤100ms

---

## 4) Non-Functional Requirements

**Portability:** Python 3.9+ with Tkinter on Windows, macOS, Linux

**Reliability:** Atomic file writes (temp file → rename) prevent data loss

**Data Integrity:** UTF-8 only, normalized whitespace

**Usability:** Zero configuration, clear empty states

**Maintainability:** MVC architecture separates model, view, and controller

---

## 5) Design Constraints

- Task length: 1-100 characters (trimmed)
- Soft limit: 1,000 total tasks
- Storage: single `todo.json` file
- Stack: Python standard library only
- Window: resizable, 480×360 minimum

---

## 6) Data Model
```json
{
  "active": ["newest task", "older task"],
  "completed": ["done task"]
}
```

Tasks ordered newest-first. Text is unique identifier (no IDs in MVP).

---

## 7) Acceptance Tests

1. **Valid add:** Enter "walk dog" → appears in Active, saved to file
2. **Empty reject:** Enter spaces → shows "Please enter a task"
3. **Duplicate reject:** Add existing task → shows "Task already exists"
4. **Complete:** Check "walk dog" → moves to Completed, saves
5. **Persistence:** Add tasks, complete one, restart → state restored

---

## Out of Scope

Editing, deleting, due dates, priority, search, multi-user, sync, notifications, themes.