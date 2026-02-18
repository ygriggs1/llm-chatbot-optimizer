"""
Example script demonstrating how to use the crypto wallet prompt with OpenAI API
This script loads the prompt and generates crypto wallet code using GPT-4
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_prompt(prompt_file):
    """Load the crypto wallet prompt from file"""
    with open(prompt_file, 'r', encoding='utf-8') as f:
        return f.read()

def generate_crypto_wallet_code(prompt, model="gpt-4-turbo-preview", max_tokens=4096):
    """
    Generate crypto wallet code using the provided prompt
    
    Args:
        prompt: The detailed prompt for code generation
        model: OpenAI model to use (default: gpt-4-turbo-preview)
        max_tokens: Maximum tokens in response (default: 4096)
    
    Returns:
        Generated code and explanations
    """
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    try:
        print(f"🚀 Generating crypto wallet code with {model}...")
        print(f"📝 Prompt length: {len(prompt)} characters\n")
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system", 
                    "content": "You are an expert full-stack blockchain developer with deep expertise in cryptocurrency wallet development, smart contract integration, and secure payment systems."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0.7,  # Balanced creativity and consistency
            max_tokens=max_tokens,
            top_p=0.95
        )
        
        generated_code = response.choices[0].message.content
        
        # Print statistics
        print(f"✅ Generation complete!")
        print(f"📊 Response length: {len(generated_code)} characters")
        print(f"🔢 Tokens used: {response.usage.total_tokens}")
        print(f"   - Prompt tokens: {response.usage.prompt_tokens}")
        print(f"   - Completion tokens: {response.usage.completion_tokens}")
        
        return generated_code
        
    except Exception as e:
        print(f"❌ Error generating code: {str(e)}")
        return None

def generate_in_stages(prompt_file):
    """
    Generate code in stages to manage token limits
    This approach breaks the generation into smaller, focused tasks
    """
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Load base prompt
    base_prompt = load_prompt(prompt_file)
    
    stages = [
        {
            "name": "Frontend Components",
            "focus": "Generate only the React frontend components with TypeScript for the crypto wallet, including WalletDashboard, SendTransaction, ReceiveTokens, TransactionHistory, and WalletConnect components."
        },
        {
            "name": "Backend API",
            "focus": "Generate the Node.js + Express backend with all API endpoints, controllers, and services for wallet management and transactions."
        },
        {
            "name": "Configuration & Setup",
            "focus": "Generate all configuration files including package.json, tsconfig.json, .env.example, Dockerfile, and docker-compose.yml."
        },
        {
            "name": "Tests & Documentation",
            "focus": "Generate comprehensive test suite using Jest and complete documentation including README.md and API documentation."
        }
    ]
    
    results = {}
    
    for stage in stages:
        print(f"\n{'='*60}")
        print(f"📦 Stage: {stage['name']}")
        print(f"{'='*60}\n")
        
        stage_prompt = f"{base_prompt}\n\n## Current Focus\n{stage['focus']}\n\nGenerate only this part with complete implementation."
        
        try:
            response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "You are an expert full-stack blockchain developer."},
                    {"role": "user", "content": stage_prompt}
                ],
                temperature=0.7,
                max_tokens=4096
            )
            
            results[stage['name']] = response.choices[0].message.content
            print(f"✅ {stage['name']} generated successfully")
            print(f"🔢 Tokens used: {response.usage.total_tokens}")
            
        except Exception as e:
            print(f"❌ Error in {stage['name']}: {str(e)}")
            results[stage['name']] = None
    
    return results

def save_generated_code(code, output_dir="generated_wallet"):
    """Save the generated code to files"""
    import os
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the full output
    output_file = os.path.join(output_dir, "generated_code.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(code)
    
    print(f"\n💾 Generated code saved to: {output_file}")
    
    # Parse and save individual files (basic implementation)
    # In a real scenario, you'd parse code blocks and save them to appropriate files
    print(f"📁 Output directory: {output_dir}")

def main():
    """Main execution function"""
    print("="*60)
    print("🏦 Crypto Wallet Code Generator")
    print("="*60)
    print()
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please set it in your .env file or environment")
        return
    
    # Path to the prompt file
    prompt_file = "examples/crypto_wallet_prompt.txt"
    
    if not os.path.exists(prompt_file):
        print(f"❌ Error: Prompt file not found: {prompt_file}")
        return
    
    # Choose generation method
    print("Choose generation method:")
    print("1. Single request (complete prompt)")
    print("2. Staged generation (multiple focused requests)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        # Load and use the complete prompt
        prompt = load_prompt(prompt_file)
        generated_code = generate_crypto_wallet_code(prompt)
        
        if generated_code:
            save_generated_code(generated_code)
            print("\n✨ Generation complete! Review the output and iterate as needed.")
    
    elif choice == "2":
        # Generate in stages
        results = generate_in_stages(prompt_file)
        
        # Save each stage
        for stage_name, code in results.items():
            if code:
                stage_dir = f"generated_wallet/{stage_name.lower().replace(' ', '_')}"
                os.makedirs(stage_dir, exist_ok=True)
                output_file = os.path.join(stage_dir, "code.txt")
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(code)
                print(f"💾 {stage_name} saved to: {output_file}")
        
        print("\n✨ Staged generation complete!")
    
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
