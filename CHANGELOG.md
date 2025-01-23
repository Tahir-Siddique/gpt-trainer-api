# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2025-01-23
### Added
- Added `stream_message` method to `MessageAPI`:
  - Supports real-time streaming of chatbot responses from the GPT Trainer API.
  - Returns concatenated streamed response as a single string.
- Added full support for managing session messages, including:
  - Listing messages (`list_messages`).
  - Deleting individual messages (`delete_message`).
  - Bulk deleting messages (`bulk_delete_messages`).

### Changed
- Improved error handling and documentation for `MessageAPI`.

---

## [0.2.0] - 2025-01-23
### Added
- Implemented full support for Data Sources, including:
  - File upload
  - Adding QA pairs
  - Adding URLs
  - Bulk deletion of sources
  - Re-scraping URLs.
- Unified API client `GPTTrainerAPI` for easy access to all APIs.

### Changed
- Improved `source_api.py` with additional methods for managing data sources.

---

## [0.1.0] - 2025-01-20
### Added
- Initial release of `gpt_trainer_api`:
  - Chatbot management.
  - Agent management.
  - Session creation and message handling.
  - Basic data source management.
