import os
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TEMPLATE = '/home/blanta/Desktop/development/resume-factory/ResumeFormatGuides/John.R.Kosinski.docx'
OUTPUT = '/home/blanta/Desktop/development/resume-factory/TailoredResumes/Solace-TechnicalLead/Resume.docx'

def bullet(doc, text):
    p = doc.add_paragraph(text, style='Normal')
    pPr = p._p.get_or_add_pPr()
    numPr = OxmlElement('w:numPr')
    ilvl = OxmlElement('w:ilvl')
    ilvl.set(qn('w:val'), '0')
    numId = OxmlElement('w:numId')
    numId.set(qn('w:val'), '5')
    numPr.append(ilvl)
    numPr.append(numId)
    pPr.append(numPr)
    return p

def n(doc, text=''):
    return doc.add_paragraph(text, style='Normal')

doc = Document(TEMPLATE)

# Clear body content (keep section properties)
for el in list(doc.element.body):
    if el.tag != qn('w:sectPr'):
        doc.element.body.remove(el)

# Name
doc.add_heading('JOHN R. KOSINSKI', level=1)

# Subtitle and contact
n(doc, 'Technical Lead • Senior Full-Stack Engineer • Team Builder')
n(doc, 'john.kosinski@gmail.com')

# SUMMARY
doc.add_heading('SUMMARY', level=2)
n(doc, 'Senior full-stack engineer and technical lead with a decade of experience shipping consumer-facing products at startup pace. Served as CTO and co-founder of a live multitenant e-commerce marketplace, leading six engineers while remaining hands-on with architecture, code review, and production delivery across TypeScript, NestJS, TypeORM, React, PostgreSQL, and Redis. Comfortable splitting time between direct coding output and unblocking, mentoring, and reviewing the work of a team.')
n(doc, 'Primary strengths include full-stack TypeScript delivery from database models through polished consumer-facing interfaces, direct engineering team management and mentorship, and creating technical structure in ambiguous, fast-moving startup environments.')

# CORE CAPABILITIES
doc.add_heading('CORE CAPABILITIES', level=2)
for cap in [
    'Full-stack TypeScript/Node/React product delivery (NestJS, TypeORM, PostgreSQL, Redis, Tailwind)',
    'Direct engineering team leadership, mentorship, and people management (2–6 engineers)',
    'Consumer-facing feature delivery from database models through UI components',
    'End-to-end architecture ownership for major product initiatives',
    'Production engineering: CI/CD, automated tests, environments, monitoring, alerting',
    'Event-driven systems and API design (REST, WebSockets, cloud-native)',
    'Cross-functional execution with product and design partners',
    'LLM-assisted systems and AI integration into production workflows',
    'Constraint-driven architecture under real-world operational risk',
]:
    bullet(doc, cap)

# SYSTEMS OWNED / SELECTED EXPERIENCE
doc.add_heading('SYSTEMS OWNED / SELECTED EXPERIENCE', level=2)

# Hamza
doc.add_heading('Hamza - CTO and Co-Founder', level=3)
n(doc, 'January 2024 – January 2026')
for b in [
    'Led a six-developer engineering team as CTO and co-founder, managing frontend, backend, seller admin, payment infrastructure, and smart-contract workstreams while remaining hands-on with implementation, code review, and architecture on a continuous delivery cadence',
    'Architected and helped deliver a production multitenant e-commerce marketplace using NestJS, TypeScript, TypeORM, Next.js, React, PostgreSQL, Redis, Tailwind CSS, and Kubernetes on AWS, supporting hundreds of monthly users, 20+ sellers, and thousands of SKUs',
    'Owned full-stack feature delivery from database models through NestJS APIs to Next.js/React storefronts and Vite-based seller admin tooling - including inventory, cart, wishlist, user management, preferences, notifications, and buyer/seller workflows',
    'Established production engineering practices across the team: CI/CD, backend tests, payment-system tests, dev/staging/testing environments, monitoring, alerting, repository management, and structured code review',
    'Coordinated delivery across a TypeScript monorepo with shared packages, EventBridge/SQS event processing, and AWS infrastructure while balancing executive technical strategy with direct engineering execution at startup pace',
]:
    bullet(doc, b)

# Stream Finance
doc.add_heading('Stream Finance - Principal Architect and Founding Engineer', level=3)
n(doc, '2022 – 2023')
for b in [
    'Served as principal architect and founding engineer for Stream Finance, owning TypeScript/Node.js backend and cloud operations infrastructure for a production investment protocol from initial design through production deployment',
    'Managed a frontend developer delivering the admin dashboard, overseeing delivery, design alignment, and code quality while owning the broader backend, security, and operations architecture',
    'Architected AWS-backed operational services around the protocol: event-driven deposit finalization, lifecycle management, exchange-rate processing, audit logging, and CloudWatch monitoring and alerting',
    'Built a multi-layer testing strategy covering unit tests, integration tests, randomized multi-user round simulations, and invariant testing, operating under capital-at-risk correctness requirements',
    'System became the technical foundation for XUSD, a same-company stablecoin product with six-figure real-money financial exposure',
]:
    bullet(doc, b)

# Private Client
doc.add_heading('Private Client - AI/Trading Systems Engineer', level=3)
n(doc, 'January 2026 – Present')
for b in [
    'Sole architect and developer of a live, real-money prediction-markets trading platform using TypeScript, Python, PostgreSQL, Vite, and Tailwind CSS, supporting live trading on Kalshi and Polymarket, historical backtesting, and Bayesian parameter optimization',
    'Designed a modular TypeScript strategy framework where each strategy is implemented as a class behind a shared interface, enabling consistent backtesting, optimization, comparison, and live execution across multiple strategy families',
    'Built a TypeScript/Vite/Tailwind frontend exposing saved backtests, optimization runs, live trading sessions, account data, strategy dashboards, and live trading controls with AI-assisted strategy generation',
    'Embedded lightweight LLM-wrapper agents for strategy analysis, diagnostic parsing, backtest interpretation, and parameter tuning - integrating AI assistance into production trading workflows without heavyweight orchestration complexity',
]:
    bullet(doc, b)

# Budgie
doc.add_heading('Budgie - Technical Software Architect (Discovery Engagement)', level=3)
n(doc, 'April – May 2026')
for b in [
    'Served as Technical Software Architect on a formal Toptal discovery engagement for Budgie, an AI-powered personal finance startup, as the technical member of a 3-person cross-functional team (architect, product manager, UI/UX designer)',
    'Designed full-stack consumer platform architecture across bank data ingestion, financial core services, AI coaching, notifications pipeline, user/auth services, and admin console - producing six C4-level architecture diagrams for the build-phase handoff team',
    'Designed a layered LLM orchestration architecture (Personality, Guardrails, deterministic calculation Tools, Context, PII Detection, Explainability) preventing hallucination in financial AI outputs for a consumer-facing coaching product',
    'Contributed technical scoping to a 421-feature product backlog across 16 epics, translating consumer product requirements into executable architecture, vendor assessments, and build-phase estimates',
]:
    bullet(doc, b)

# ADDITIONAL EXPERIENCE
doc.add_heading('ADDITIONAL EXPERIENCE', level=2)
for item in [
    'PFP Capital (Solana Low-Latency Copy-Trading, Rust/React 18/TypeScript, 2025–Present)',
    'Skunk Capital (Automated Trading Systems, NodeJS/React, 2017–2019)',
    'Soundbeats (GameFi Engineering, Blockchain)',
    'Morgan Stanley',
    'Aquamonix',
    'Leeds Rising',
    'Manao Software',
    'HotelTravel',
]:
    bullet(doc, item)
n(doc, '(Details intentionally compressed; full history available on request)')

# OPERATING PRINCIPLES
doc.add_heading('OPERATING PRINCIPLES', level=2)
for p in [
    'Own the outcome, not just the implementation',
    'Design for failure modes before success cases',
    'Prefer irreversible correctness over reversible speed when capital is at risk',
    'Direct and clear communication',
]:
    bullet(doc, p)

# TOOLS & TECHNOLOGIES
doc.add_heading('TOOLS & TECHNOLOGIES (SELECTED)', level=2)
for t in [
    'TypeScript',
    'NestJS / Node.js',
    'React (Next.js, React 18)',
    'PostgreSQL',
    'Redis',
    'Tailwind CSS',
    'Python',
    'AWS, GCP',
    'Kubernetes',
    'Vite / TanStack Query',
    'LLM Integration / AI Agents',
    'Solidity',
    'Rust',
    'Kafka',
]:
    bullet(doc, t)

# AVAILABILITY
doc.add_heading('AVAILABILITY', level=2)
n(doc, 'Technical lead roles combining hands-on full-stack TypeScript engineering with direct people management - consumer-facing products, startup pace, TypeScript/Node/React environments.')

# CITIZENSHIP
doc.add_heading('CITIZENSHIP', level=2)
n(doc, 'US Citizen')

doc.save(OUTPUT)
print(f'Saved: {OUTPUT}')
