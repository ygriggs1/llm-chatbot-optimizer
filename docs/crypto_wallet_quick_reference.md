# Quick Reference: $PIUSD Crypto Wallet Prompt

## 🚀 Quick Start Prompt

Copy and paste this optimized prompt to generate a complete crypto wallet:

---

**You are an expert full-stack blockchain developer.** Generate production-ready code for a **$PIUSD cryptocurrency wallet** that integrates with https://patxilanoix.com/ via Kimi website maker.

### Token Details
- **Token**: $PIUSD_PATXI
- **ID**: 14nfWewQNEjPo4Qj3i7xBkS6TnVStvZpgbVtNruvmusD
- **Blockchain**: Solana (mainnet-beta)

### Frontend Stack
- React 18+ with TypeScript
- Tailwind CSS + shadcn/ui
- @solana/web3.js + @solana/wallet-adapter-react
- State: Redux Toolkit or Zustand

### Backend Stack
- Node.js 18+ with TypeScript
- Express.js or Fastify
- PostgreSQL + Prisma ORM
- Redis for caching
- JWT authentication

### Required Features

**Frontend Components:**
1. Wallet connection (Phantom, Solflare)
2. Balance display with real-time updates
3. Send tokens interface with validation
4. Receive tokens with QR code
5. Transaction history (last 20)
6. Responsive design (mobile/desktop)
7. Dark/light theme
8. Loading states and error handling

**Backend Endpoints:**
1. `POST /api/wallet/create` - Create wallet
2. `GET /api/wallet/:address/balance` - Get balance
3. `POST /api/transactions/send` - Send transaction
4. `GET /api/transactions/history/:address` - Transaction history
5. `POST /api/auth/verify-signature` - Verify wallet signature
6. `GET /api/token/info` - Token information

**Security Requirements:**
- Never store private keys
- Web3 signature verification
- Input validation (addresses, amounts)
- Rate limiting on all endpoints
- HTTPS/TLS only
- CORS configuration
- Helmet.js for headers
- Error handling without sensitive info leaks

**Integration for Kimi:**
Provide widget embedding code:
```html
<div id="piusd-wallet"></div>
<script src="https://patxilanoix.com/wallet/widget.js"></script>
<script>
  PIUSDWallet.init({
    containerId: 'piusd-wallet',
    network: 'mainnet-beta',
    tokenAddress: '14nfWewQNEjPo4Qj3i7xBkS6TnVStvZpgbVtNruvmusD'
  });
</script>
```

### Code Quality Standards
- TypeScript strict mode (no 'any')
- ESLint + Prettier configured
- Jest tests with 70% coverage
- Proper error handling with try-catch
- JSDoc comments for complex functions
- Semantic Git commit messages

### Deliverables
1. Complete frontend code (components, hooks, services, types)
2. Complete backend code (routes, controllers, middleware, models)
3. Configuration files (package.json, tsconfig.json, .env.example)
4. Docker setup (Dockerfile, docker-compose.yml)
5. README.md with setup instructions
6. API documentation
7. Test suite
8. Deployment guide

### File Structure

**Frontend:**
```
src/
├── components/
│   ├── WalletDashboard.tsx
│   ├── SendTransaction.tsx
│   ├── ReceiveTokens.tsx
│   ├── TransactionHistory.tsx
│   └── WalletConnect.tsx
├── hooks/
│   ├── useWallet.ts
│   └── useTransactions.ts
├── services/
│   └── solanaService.ts
├── types/
│   └── wallet.types.ts
└── utils/
    ├── validation.ts
    └── formatters.ts
```

**Backend:**
```
src/
├── routes/
│   ├── wallet.routes.ts
│   ├── transaction.routes.ts
│   └── auth.routes.ts
├── controllers/
│   ├── wallet.controller.ts
│   └── transaction.controller.ts
├── services/
│   ├── solana.service.ts
│   └── cache.service.ts
├── middleware/
│   ├── auth.middleware.ts
│   └── validation.middleware.ts
└── models/
    ├── wallet.model.ts
    └── transaction.model.ts
```

### Performance Targets
- Initial load: < 3 seconds
- API response: < 500ms (p95)
- Transaction confirmation: < 2 seconds

### Priority Order
1. **MVP**: Wallet connect, balance, send/receive
2. **Enhanced**: History, notifications, security
3. **Advanced**: Analytics, optimization

Generate the complete, production-ready implementation with all files, configurations, and documentation.

---

## 📝 Usage Tips

### For GPT-4/Claude
- Copy the entire prompt above
- Submit in a single message
- Request specific sections if output is truncated

### For Iterative Development
Ask for components in stages:
1. "Generate frontend components first"
2. "Now generate backend API"
3. "Now generate configuration and deployment files"

### For Code Review
After generation, ask:
- "Review the code for security vulnerabilities"
- "Check for TypeScript type errors"
- "Verify Solana blockchain integration"

## 🔄 Customization

To adapt for different tokens:

1. **Change token details**:
   - Token ID/contract address
   - Blockchain (Ethereum, Polygon, etc.)
   - Token standard (ERC-20, SPL)

2. **Update libraries**:
   - Solana → Ethereum: `@solana/web3.js` → `ethers.js`
   - Phantom → MetaMask: `@solana/wallet-adapter` → `wagmi`

3. **Adjust integration**:
   - Update website URL
   - Change builder platform

## ⚡ Common Follow-ups

After initial generation, you might ask:

- "Add multi-language support (Spanish, French)"
- "Implement token swap functionality"
- "Add hardware wallet support (Ledger)"
- "Create admin dashboard for monitoring"
- "Add NFT display capabilities"
- "Implement staking interface"

## 🐛 Troubleshooting

If generated code has issues:

**Issue**: Missing dependencies
**Fix**: "Add package.json with all required dependencies"

**Issue**: TypeScript errors
**Fix**: "Fix TypeScript errors and add proper type definitions"

**Issue**: No tests
**Fix**: "Generate comprehensive test suite with Jest"

**Issue**: Security concerns
**Fix**: "Review and fix security vulnerabilities, add rate limiting"

## 📊 Success Metrics

Evaluate the generated code:
- ✅ All files generated
- ✅ No TypeScript errors
- ✅ Passes ESLint
- ✅ 70%+ test coverage
- ✅ No critical security issues
- ✅ Builds successfully
- ✅ Documentation complete

---

**Version**: 1.0.0 | **Updated**: 2026-02-18
