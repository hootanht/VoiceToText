# GitHub Secrets Setup Guide
# راهنمای تنظیم رازهای گیت‌هاب

This guide explains how to set up GitHub secrets for your Voice to Text Analyzer project.

## 🔐 Why GitHub Secrets?

GitHub secrets allow you to:
- Store sensitive information (API keys) securely
- Keep credentials out of your code repository
- Use real API keys in CI/CD without exposing them
- Enable integration testing with actual services

## 📝 Required Secrets

You need to set up these secrets in your GitHub repository:

| Secret Name | Description | Example Value |
|-------------|-------------|---------------|
| `GEMINI_API_KEY` | Your Google Gemini API key | `AIzaSyB...` |
| `GEMINI_MODEL_NAME` | Gemini model to use | `gemini-2.0-flash` |

## 🚀 How to Set Up GitHub Secrets

### Step 1: Go to Your Repository Settings

1. Navigate to your GitHub repository
2. Click on **Settings** tab
3. In the left sidebar, click **Secrets and variables**
4. Click **Actions**

### Step 2: Add Repository Secrets

1. Click **New repository secret**
2. Add the following secrets:

#### GEMINI_API_KEY
- **Name**: `GEMINI_API_KEY`
- **Secret**: Your actual Google Gemini API key
- Click **Add secret**

#### GEMINI_MODEL_NAME
- **Name**: `GEMINI_MODEL_NAME`
- **Secret**: `gemini-2.0-flash` (or your preferred model)
- Click **Add secret**

## 🔑 Getting Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **Create API Key**
4. Copy the generated API key
5. Use this key as your `GEMINI_API_KEY` secret

## ✅ Verification

After setting up the secrets, your GitHub Actions will:

1. **Use real API keys** when secrets are available
2. **Fall back to test keys** when secrets are not set
3. **Run successfully** in both scenarios

## 🔄 How It Works in GitHub Actions

Your workflows now use this pattern:

```yaml
echo "GEMINI_API_KEY=${{ secrets.GEMINI_API_KEY || 'test_key_for_ci' }}" >> .env
```

This means:
- ✅ If `GEMINI_API_KEY` secret exists → use real API key
- ✅ If secret doesn't exist → use fallback test key
- ✅ Tests will pass in both cases

## 🛡️ Security Best Practices

### DO ✅
- Use GitHub secrets for real API keys
- Keep your `.env` file in `.gitignore`
- Use descriptive secret names
- Rotate API keys regularly

### DON'T ❌
- Never commit API keys to your repository
- Don't share secrets in issues or discussions
- Don't use secrets in public repositories unless necessary
- Don't hardcode sensitive values

## 🧪 Testing Your Setup

### With Secrets (Integration Testing)
When secrets are set, your actions will:
- Use real Gemini API
- Run actual integration tests
- Validate API connectivity

### Without Secrets (Unit Testing)
When secrets are not set, your actions will:
- Use mocked responses
- Run fast unit tests
- No API calls made

## 🔧 Local Development

For local development, create a `.env` file:

```bash
# .env (DO NOT COMMIT THIS FILE)
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL_NAME=gemini-2.0-flash
```

Make sure `.env` is in your `.gitignore`:

```gitignore
# Environment files
.env
.env.local
.env.*.local
```

## 📊 Monitoring

You can monitor secret usage:
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Check **Recent activity** to see when secrets were accessed
3. Review **Actions** tab to see workflow runs

## 🆘 Troubleshooting

### Problem: Tests fail with API errors
**Solution**: Check if your API key is valid and has proper permissions

### Problem: Secrets not working in forks
**Solution**: Secrets are not passed to workflows in forks for security reasons

### Problem: API quota exceeded
**Solution**: Monitor your API usage in Google AI Studio console

## 📞 Support

If you encounter issues:
1. Check the **Actions** tab for detailed error logs
2. Verify your API key in Google AI Studio
3. Ensure secrets are spelled correctly
4. Check if your repository has the required secrets set

---

## 🎯 Quick Setup Checklist

- [ ] Created `GEMINI_API_KEY` secret
- [ ] Created `GEMINI_MODEL_NAME` secret  
- [ ] Verified secrets are accessible in repository settings
- [ ] Triggered a workflow run to test the setup
- [ ] Confirmed tests pass with real API integration

**🎉 Your GitHub Actions are now configured to use GitHub secrets securely!** 