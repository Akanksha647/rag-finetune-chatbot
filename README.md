 git init                          
Reinitialized existing Git repository in C:/Users/keshaa2/OneDrive - Dell Technologies/rag-finetune-chatbot/.git/
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> git add .                         
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> rmdir /s /q rag-finetune-chatbot^C
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> git commit -m "Initial RAG chatbot project"
[master (root-commit) 033866e] Initial RAG chatbot project
 Committer: Kesharwani <akanksha.kesharwani@dell.com>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 7 files changed, 184 insertions(+)
 create mode 100644 app.py
 create mode 100644 data/company_docs.txt
 create mode 100644 finetune_data.jsonl
 create mode 100644 ingest.py
 create mode 100644 rag_chat.py
 create mode 100644 requirements.txt
 create mode 100644 train_qlora.py
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> ^C
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> git remote -v
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> git branch -M main
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> git remote add origin https://github.com/Akanksha647/rag-finetune-chatbot.git
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> git push -u origin main
info: please complete authentication in your browser...
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 22 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (10/10), 3.08 KiB | 185.00 KiB/s, done.
Total 10 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Akanksha647/rag-finetune-chatbot.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(venv) PS C:\Users\keshaa2\OneDrive - Dell Technologies\rag-finetune-chatbot> 
