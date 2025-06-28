# 🏙️ CivicSpotter

**A Smart Civic Issue Reporting & Management Platform**

CivicSpotter is an intelligent crowdsourced platform that empowers citizens to report local infrastructure issues through simple photo uploads while providing administrators with powerful tools to manage, track, and resolve these issues efficiently.

## 🌟 Key Features

### 👥 For Citizens
- **📸 Photo-Based Reporting**: Upload photos directly from camera or gallery
- **🗺️ Automatic Location Detection**: GPS-based location extraction from photos or browser
- **🔍 Issue Tracking**: Search and track your submitted issues by ID
- **📱 Mobile-Friendly Interface**: Responsive design for all devices
- **🤝 Smart Duplicate Detection**: Automatically groups similar nearby issues

### 🛠️ For Administrators
- **📋 Comprehensive Dashboard**: Review and manage all reported issues
- **✅ Multi-Stage Approval Process**: Metadata → Authority → Tweet review workflow
- **📧 Automated Email Generation**: Smart authority contact discovery and email composition
- **🐦 Social Media Integration**: Automated tweet generation and posting to amplify issues
- **🔍 Advanced Filtering**: Filter issues by stage, city, and status
- **📊 Real-time Status Tracking**: Monitor issue progress from submission to resolution

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Upload   │───▶│  Metadata        │───▶│  Admin Review   │
│   (Photo +      │    │  Extraction      │    │  & Approval     │
│    Location)    │    │  & Processing    │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Similar       │    │   Authority      │    │   Email &       │
│   Issue         │    │   Contact        │    │   Tweet         │
│   Detection     │    │   Discovery      │    │   Generation    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Required API keys (see Configuration section)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CivicSpotter.git
   cd CivicSpotter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and credentials
   ```

4. **Create required directories**
   ```bash
   mkdir -p issues/active issues/completed temp_uploads
   ```

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

## ⚙️ Configuration

### Required API Keys

Create a `.env` file with the following credentials:

```env
# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Twitter API (for social media integration)
TWITTER_API_KEY=your-api-key
TWITTER_API_SECRET=your-api-secret
TWITTER_ACCESS_TOKEN=your-access-token
TWITTER_ACCESS_SECRET=your-access-secret
TWITTER_BEARER_TOKEN=your-bearer-token

# Google AI (for content generation)
GOOGLE_API_KEY=your-google-ai-key

# Tavily Search (for authority discovery)
TAVILY_API_KEY=your-tavily-key

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD_HASH=your-sha256-hashed-password
```

### API Setup Instructions

1. **Google AI API**: Get your key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Twitter API**: Apply for developer access at [Twitter Developer Portal](https://developer.twitter.com/)
3. **Tavily Search**: Sign up at [Tavily](https://tavily.com/) for web search capabilities
4. **Email**: Use Gmail with App Password or configure your SMTP provider

## 📱 Usage Guide

### For Citizens

1. **Report an Issue**
   - Navigate to User Dashboard
   - Choose "Take photo" or "Upload from gallery"
   - Select issue type (Pothole, Garbage, Water Leakage, etc.)
   - Submit with automatic location detection

2. **Track Your Issue**
   - Use the Issue ID provided after submission
   - Search on the main page to see current status
   - View if your issue was merged with similar reports

### For Administrators

1. **Login**
   - Use admin credentials on the sidebar
   - Access the Admin Dashboard

2. **Review Process**
   - **Metadata Review**: Verify and edit extracted location data
   - **Authority Review**: Confirm authority contact information
   - **Tweet Review**: Review and edit generated social media content

3. **Approval Workflow**
   - Approve each stage to proceed to the next
   - System automatically processes approved stages
   - Monitor errors and retry failed operations

## 🔧 Core Components

### 📊 Issue Management (`src/manage_issue/`)
- **IssueState**: Manages issue lifecycle and storage
- **SimilarIssueFinder**: Detects and groups related issues
- **StateTemplate**: Defines issue data structure

### 📍 Metadata Extraction (`src/photo_extractor.py`)
- Extracts GPS coordinates from EXIF data
- Reverse geocoding for address information
- Fallback to browser GPS for camera uploads

### 🔍 Authority Discovery (`authority_finder/`)
- **TavilySearch**: Web search for authority contacts
- **AuthorityFinder**: AI-powered contact extraction
- Smart query generation for local authorities

### 📧 Communication (`Email/`, `Social_platforms/`)
- **EmailNotifier**: Automated email composition and sending
- **TwitterIntegration**: Tweet generation and posting
- Professional templates with embedded images

### 🧠 Orchestration (`coordinator/orchestrator.py`)
- **TheBrain**: Central coordinator managing the entire workflow
- Stage management and approval processing
- Error handling and retry mechanisms

## 📁 Project Structure

```
CivicSpotter/
├── 📁 src/                     # Core application logic
│   ├── manage_issue/           # Issue lifecycle management
│   ├── photo_extractor.py      # Metadata extraction
│   └── unique_id.py           # ID generation
├── 📁 authority_finder/        # Authority contact discovery
├── 📁 Email/                   # Email communication
├── 📁 Social_platforms/        # Social media integration
├── 📁 coordinator/             # Workflow orchestration
├── 📁 pages/                   # Streamlit UI pages
├── 📁 issues/                  # Issue storage
│   ├── active/                 # Pending issues
│   └── completed/              # Resolved issues
├── main.py                     # Application entry point
└── requirements.txt            # Dependencies
```

## 🔄 Workflow Process

1. **Issue Submission**
   - User uploads photo with location data
   - System extracts metadata and generates unique ID
   - Similar issue detection prevents duplicates

2. **Admin Review Stages**
   - **Stage 1**: Metadata verification and editing
   - **Stage 2**: Authority contact confirmation
   - **Stage 3**: Tweet content review and approval

3. **Automated Actions**
   - Email sent to relevant civic authority
   - Tweet posted to amplify the issue
   - Issue moved to completed status

4. **Tracking & Follow-up**
   - Citizens can track progress via Issue ID
   - Admins monitor resolution status
   - Social media provides public accountability

## 🛡️ Security Features

- **Admin Authentication**: SHA-256 password hashing
- **Data Validation**: Input sanitization and validation
- **File Security**: Secure image upload handling
- **API Security**: Environment-based credential management

## 🔧 Advanced Features

### Smart Duplicate Detection
- Geographic proximity analysis (configurable radius)
- Issue type matching
- Postal code-based grouping
- Automatic image aggregation for similar issues

### AI-Powered Content Generation
- Context-aware email templates
- Professional tweet composition
- Authority contact discovery
- Location-specific query generation

### Robust Error Handling
- Retry mechanisms for failed operations
- Comprehensive error logging
- Graceful degradation for missing data
- User-friendly error messages

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Documentation**: Check the code comments for detailed implementation notes
- **Community**: Join discussions in the repository

## 🙏 Acknowledgments

- **Streamlit** for the amazing web framework
- **Google AI** for intelligent content generation
- **Twitter API** for social media integration
- **OpenStreetMap/Nominatim** for geocoding services
- **Tavily** for web search capabilities

---

**Built with ❤️ for better civic engagement and community empowerment**

*CivicSpotter - Making cities more responsive, one photo at a time.*