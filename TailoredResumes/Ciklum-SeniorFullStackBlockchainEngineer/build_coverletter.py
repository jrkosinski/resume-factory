"""Build CoverLetter.docx for the Ciklum application."""

from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TEMPLATE = "/home/blanta/NOWY/projects/resume-factory/ResumeFormatGuides/John.R.Kosinski.docx"
OUTPUT = "/home/blanta/NOWY/projects/resume-factory/TailoredResumes/Ciklum-SeniorFullStackBlockchainEngineer/CoverLetter.docx"

doc = Document(TEMPLATE)

for p in list(doc.paragraphs):
    p._element.getparent().remove(p._element)


def h1(doc, text):
    return doc.add_paragraph(text, style="Heading 1")


def h2(doc, text):
    return doc.add_paragraph(text, style="Heading 2")


def n(doc, text):
    return doc.add_paragraph(text, style="Normal")


# Header
h1(doc, "JOHN R. KOSINSKI")
n(doc, "john.kosinski@gmail.com")
n(doc, "")

n(doc, "Dear Ciklum Hiring Team,")
n(doc, "")

n(doc, (
    "I am writing to apply for the Senior Full Stack (Blockchain) Engineer position. My background "
    "maps closely to what you have described: production experience building multi-chain backend "
    "infrastructure in TypeScript and Node.js, deep DeFi protocol knowledge across EVM and non-EVM "
    "chains, and a security-first engineering culture shaped by years of working on systems where "
    "correctness under financial risk is non-negotiable."
))
n(doc, "")

n(doc, (
    "Some specific points of alignment with your requirements:"
))
n(doc, "")

n(doc, (
    "As CTO and Co-Founder of Hamza, I architected and delivered a production cross-chain crypto "
    "payment system spanning Optimism, Arbitrum, Ethereum mainnet, Bitcoin, Polygon, Mantle, and "
    "Scroll. The backend was built around NestJS microservices in TypeScript, with Ethers.js v6 for "
    "EVM chains, @solana/web3.js for Solana support, and LiFi for cross-chain bridging and batch "
    "settlement. Payment flows ran through an event-driven pipeline over EventBridge and SQS, with "
    "HD-wallet-derived deposit addresses, idempotent state machine processing, and Solidity escrow "
    "contracts secured by Echidna property-based fuzzing."
))
n(doc, "")

n(doc, (
    "On the non-EVM side, I built and currently operate a live real-money Solana trading system for "
    "PFP Capital, integrating Jupiter DEX aggregator routing, Pump.fun bonding-curve execution, and "
    "Jito tip routing for priority execution. The system includes on-chain data indexing via the "
    "Helius enhanced transaction API, parsing swaps across 11 Solana DEXs."
))
n(doc, "")

n(doc, (
    "Earlier, as founding engineer and principal architect at Stream Finance, I designed an EVM-based "
    "tokenized Treasury bond DeFi protocol that secured hundreds of millions USD in TVL and later "
    "became the foundation for a same-company stablecoin. That project reinforced how important "
    "testing depth, access control, and invariant verification are in DeFi infrastructure."
))
n(doc, "")

n(doc, (
    "The kind of work Ciklum describes, building and scaling backend infrastructure and developer "
    "tooling for a platform that has onboarded tens of millions of wallets across crypto and fintech "
    "applications, is exactly the kind of high-stakes, production-scale blockchain engineering I want "
    "to be doing."
))
n(doc, "")

n(doc, (
    "I should be transparent about one practical matter: I am currently based outside Poland and would "
    "need work visa sponsorship to relocate. That said, relocation to Poland is something I genuinely "
    "want, not just a checkbox. I am of 100% Polish ancestry, and moving to Poland has been a "
    "meaningful personal goal for some time. Wroclaw and Gdansk are both cities I have researched and "
    "would be excited to live in. I mention this upfront because I want to be respectful of your time, "
    "and because I want you to know that if you are open to sponsoring a work visa, you would have "
    "someone who is committed to being in Poland for the long term, not just a temporary arrangement."
))
n(doc, "")

n(doc, "I look forward to the opportunity to discuss how my experience could contribute to what Ciklum's client is building.")
n(doc, "")
n(doc, "Sincerely,")
n(doc, "John R. Kosinski")
n(doc, "john.kosinski@gmail.com")

doc.save(OUTPUT)
print(f"Saved: {OUTPUT}")
