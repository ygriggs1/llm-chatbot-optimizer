# Crypto Wallet Prompt Examples

This directory contains advanced prompt engineering examples for generating production-ready cryptocurrency wallet applications.

## 📁 Files

### 1. `crypto_wallet_prompt.txt`
**The Complete Prompt Template**

A comprehensive, production-ready prompt for generating a full-stack $PIUSD cryptocurrency wallet. This prompt includes:

- ✅ Detailed frontend specifications (React + TypeScript)
- ✅ Complete backend requirements (Node.js + Express)
- ✅ Security best practices
- ✅ Integration instructions for Kimi website maker
- ✅ Testing and documentation requirements
- ✅ Deployment configuration
- ✅ Performance optimization guidelines

**When to use**: When you need a complete, production-ready cryptocurrency wallet application with all components.

**Token Information**:
- Token: $PIUSD_PATXI
- Contract ID: 14nfWewQNEjPo4Qj3i7xBkS6TnVStvZpgbVtNruvmusD
- Blockchain: Solana
- Target: https://patxilanoix.com/

### 2. `generate_wallet_code.py`
**Automated Code Generation Script**

A Python script that demonstrates how to use the crypto wallet prompt programmatically with OpenAI's API.

**Features**:
- Single-request generation (complete prompt)
- Staged generation (breaks into focused tasks)
- Token usage tracking
- Automatic file saving
- Error handling

**Usage**:
```bash
# Set up your API key
export OPENAI_API_KEY="your-key-here"

# Or use .env file
echo "OPENAI_API_KEY=your-key-here" > .env

# Run the generator
python examples/generate_wallet_code.py
```

### 3. `sample_prompts.txt`
**Quick Reference Examples**

Contains before/after examples showing how optimized prompts improve output quality:

- Basic prompts vs. optimized prompts
- Simple use cases (ML questions)
- Complex use case (crypto wallet generation)

**Great for**: Understanding prompt optimization principles

## 🚀 Quick Start

### Option 1: Direct LLM Usage

1. **Copy the prompt**:
   ```bash
   cat examples/crypto_wallet_prompt.txt | pbcopy  # macOS
   cat examples/crypto_wallet_prompt.txt | xclip   # Linux
   ```

2. **Paste into ChatGPT, Claude, or your LLM of choice**

3. **Review and iterate on the output**

### Option 2: Programmatic Usage

1. **Install dependencies**:
   ```bash
   pip install openai python-dotenv
   ```

2. **Set up your API key**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

3. **Run the generator**:
   ```bash
   python examples/generate_wallet_code.py
   ```

4. **Choose generation method**:
   - Option 1: Single complete generation
   - Option 2: Staged generation (recommended for large projects)

### Option 3: Custom Integration

```python
import openai
from pathlib import Path

# Load the prompt
prompt = Path("examples/crypto_wallet_prompt.txt").read_text()

# Customize for your token
prompt = prompt.replace(
    "14nfWewQNEjPo4Qj3i7xBkS6TnVStvZpgbVtNruvmusD",
    "your-token-id-here"
)

# Generate code
client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You are an expert blockchain developer."},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)
```

## 📚 Documentation

For detailed guides and best practices, see:

1. **[Crypto Wallet Prompt Guide](../docs/crypto_wallet_prompt_guide.md)**
   - Complete prompt engineering principles
   - Best practices and techniques
   - Measuring effectiveness
   - Troubleshooting guide

2. **[Quick Reference Guide](../docs/crypto_wallet_quick_reference.md)**
   - Condensed prompt version
   - Usage tips
   - Customization guide
   - Common follow-ups

## 🔧 Customization

### For Different Tokens

To adapt for Ethereum, Polygon, or other chains:

1. **Change blockchain details**:
   ```
   Blockchain: Ethereum
   Token: USDC
   Contract: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
   ```

2. **Update libraries**:
   ```
   - @solana/web3.js → ethers.js or viem
   - Phantom wallet → MetaMask
   - SPL Token → ERC-20
   ```

3. **Adjust endpoints**:
   ```
   Network: mainnet / goerli / polygon
   RPC: Your RPC endpoint
   ```

### For Different Platforms

To integrate with platforms other than Kimi:

1. **WordPress**: Provide shortcode format
2. **Webflow**: Provide custom embed code
3. **Next.js**: Provide component integration
4. **Shopify**: Provide app extension format

## 🎯 Expected Output

When using the complete prompt, you should receive:

### Frontend Files
- `App.tsx` - Main application
- `components/` - All UI components
- `hooks/` - Custom React hooks
- `services/` - API and blockchain services
- `types/` - TypeScript definitions
- `utils/` - Helper functions

### Backend Files
- `server.ts` - Express server
- `routes/` - API route handlers
- `controllers/` - Business logic
- `services/` - Core services
- `middleware/` - Auth, validation, etc.
- `models/` - Data models

### Configuration
- `package.json` - Dependencies
- `tsconfig.json` - TypeScript config
- `Dockerfile` - Container setup
- `docker-compose.yml` - Local development
- `.env.example` - Environment variables

### Documentation
- `README.md` - Setup and usage
- API documentation (OpenAPI/Swagger)
- Architecture diagrams
- Deployment guide

### Tests
- Unit tests for components
- Integration tests for APIs
- E2E tests for critical flows
- Security tests

## ⚡ Performance Tips

### Managing Token Limits

If you hit token limits:

1. **Use staged generation** (via the Python script)
2. **Request specific components**:
   ```
   "Generate only the frontend React components"
   "Generate only the backend API endpoints"
   ```
3. **Use GPT-4 with higher token limits**

### Optimizing Output Quality

1. **Be specific about versions**:
   ```
   React 18.2+
   TypeScript 5.0+
   Node.js 18+
   ```

2. **Request examples**:
   ```
   "Include example usage for each component"
   ```

3. **Specify coding standards**:
   ```
   "Follow Airbnb style guide"
   "Use functional components"
   "Implement proper error boundaries"
   ```

## 🧪 Testing the Output

After generation, validate:

```bash
# Check TypeScript
npx tsc --noEmit

# Run linter
npx eslint src/

# Run tests
npm test

# Check security
npm audit
```

## 💡 Tips for Best Results

1. **Start with the complete prompt** - Don't skip sections
2. **Review the output carefully** - LLMs can make mistakes
3. **Test incrementally** - Validate each component
4. **Iterate as needed** - Use follow-up prompts to refine
5. **Keep security in mind** - Always review security-critical code

## 🔒 Security Checklist

After code generation, verify:

- [ ] No private keys in code
- [ ] Input validation on all endpoints
- [ ] Rate limiting implemented
- [ ] HTTPS/TLS enforced
- [ ] CORS properly configured
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF tokens implemented
- [ ] Sensitive data encrypted
- [ ] Proper error handling (no info leaks)

## 📈 Success Metrics

Track these metrics:

| Metric | Target | Notes |
|--------|--------|-------|
| Files generated | 95%+ | Should include all required files |
| TypeScript errors | 0 | Must compile without errors |
| Test coverage | 70%+ | Aim for good coverage |
| Build success | ✓ | Must build successfully |
| Security issues | 0 critical | No high-severity vulnerabilities |
| Load time | < 3s | Initial page load |
| API response | < 500ms | 95th percentile |

## 🤝 Contributing

To improve these examples:

1. Test with different LLMs
2. Document results and metrics
3. Share improvements via PR
4. Add new use cases

## 📞 Support

If you encounter issues:

1. Check the [troubleshooting guide](../docs/crypto_wallet_prompt_guide.md#troubleshooting)
2. Review [common pitfalls](../docs/crypto_wallet_prompt_guide.md#common-pitfalls-to-avoid)
3. Open an issue on GitHub

## 🔗 Additional Resources

- [Solana Documentation](https://docs.solana.com/)
- [SPL Token Guide](https://spl.solana.com/token)
- [Wallet Adapter](https://github.com/solana-labs/wallet-adapter)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-18  
**Maintainer**: LLM Chatbot Optimizer Team
