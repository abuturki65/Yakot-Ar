from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio

@borg.on(admin_cmd("م14"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر التشغيل والايقاف \n\n⌔︙ الأمـر  •   `.اعادة تشغيل` \n⌔︙ الاستـخدام • لاعادة تشغيل البوت وارجاعه الى شكله الطبيعي كما كان في الاول فقط ارسل الامر\n\n⌔︙ الأمـر  •   `.تحديث`\n⌔︙ الاستـخدام • فقط ارسل الامر للتاكد اذا كان هناك تحديثات من مطورين السورس\n\n⌔︙ الامر • `.التحديثات تشغيل` \n⌔︙ الاستخدام  • يستخدم هذا الامر لارسال رسالة تجريبيه تلقائية لرؤية البوت اذا ما شغال بعد اعاده التشغيل او التحديث سيرسل امر  .بنك ولايقافه ارسل  `.التحديثات ايقاف`\n\n⌔︙ قـناة جـمثون •  \n⌔︙ @JMTHON")

@borg.on(admin_cmd("م15"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ قـائمة اوامـر المنـع\n\n⌔︙ الأمـر  •  `.منع`  <الكلمة>\n⌔︙ الاستـخدام •  بكـتابة الامر مـع كلمـة لمنعها وحذفها في الكروب تحتاج صلاحيات حذف\n\n⌔︙ الأمـر  •   `.الغاء منع `  <الكلمة> \n⌔︙ الاستـخدام •  لألـغاء منع الـكلمة والسماح بأرسالها وعدم حذفها\n\n⌔︙ الأمـر  •   `.قائمة المنع`\n⌔︙ الاستـخدام • لأظـهار قـائمة الكلمات الـممنوعه في الـمجموعه التـي ترسل بـها الامـر\n\n⌔︙ السـورس \n⌔︙ @JMTHON")

@borg.on(admin_cmd("م16"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙  اوامر التسليه\n\n⌔︙ فقط ارسل الامر وجربه \n\n⌔︙ `.قمر`\n⌔︙ `.فصخ` <الكلمة> \n ⌔︙ `.هفف`\n⌔︙ `.اقمار`\n⌔︙ `.قمور`\n⌔︙ `.قلوب`\n⌔︙ `.قلب `\n⌔︙ `.جيم`\n⌔︙ `.افكر`\n⌔︙ `.افكرر`\n⌔︙ `.شنوو `\n⌔︙ `.مح `\n⌔︙ `.متت `\n⌔︙ `.النضام الشمسي `\n⌔︙ `.موسيقى `\n ⌔︙ `.قنبله `\n⌔︙ `.مكبعات` \n⌔︙ `.افعى` \n⌔︙ `.طائره` \n⌔︙ `.نجمه` \n⌔︙ `.دائره` \n⌔︙ `.شرطه` \n⌔︙ `.فايروس` \n⌔︙ `.غبي` \n⌔︙ `.العد التنازلي`\n⌔︙ `.يد`\n⌔︙ `.تهكير`\n⌔︙ `.قرد` \n⌔︙ `.بشره` \n⌔︙ `.انيم` \n⌔︙ `.نيكول` \n⌔︙ `.مربع`\n⌔︙ `.قاتل` \n⌔︙ `.تحميل`\n⌔︙ `.رجل` \n⌔︙ `.شنوو `\n⌔︙ `.ريبي `\n⌔︙ `.تفريغ `\n⌔︙ `.حلويات `\n⌔︙ `.فليم`\n\n⌔︙ السـورس  \n⌔︙  @JMTHON")

@borg.on(admin_cmd("م17"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر الحذف والتنظيف\n\n⌔︙ الامر •  `.تنظيف  + عدد الرسائل`\n⌔︙ الاستخدام •  يقوم بحذف الرسائل اكتب الامر وعدد معين سيقوم بحذفه تحتاج صلاحيات الحذف\n⌔︙ مثـال  •  `.تنظيف 300`\n\n⌔︙ الامر  •  `.مسح`  <بالرد>\n⌔︙ الاستخدام  •  فقط اكتب الامر بالرد على الرسالة ليقوم بحذفها \n\n⌔︙ الامـر •  `.تنظيف  <الاضافة> <عدد الرسائل>`\n⌔︙ ملاحـظة  • يـجب وضع الشـارحه مع الاضافة (-)\n⌔︙ مثـال  •  `.تنظيف -ح`  <سيقوم بحذف المتحركات في الدردشة>\n⌔︙ مثـال  •  `.تنظيف -ح 50` <سيقوم بحذف اخر 50 متحركه ارسلت>\n\n⌔︙ الاضافه• \n ⌔︙-ب: لحـذف الرسائل الـصوتية\n ⌔︙-م: لحـذف الملفات\n ⌔︙-ح: لحـذف المتحـركه\n ⌔︙-ص: لحـذف الـصور\n ⌔︙-غ: لحـذف الاغاني\n ⌔︙-ق: لحـذف الـملصقات\n ⌔︙-ر: لحـذف الـروابط \n⌔︙-ف: لحـذف الفـيديوهـات\n\n⌔︙ قنـاة السـورس  :  \n ⌔︙ @JMTHON")

@borg.on(admin_cmd("م18"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر الحساب الوقتي \n\n⌔︙ الامـر  • `.اسم وقتي`  \n⌔︙ الاستخدام • فقط ارسل الامر لجلعل اسمك يتغير كل دقيقه مع تغير الوقت  \n\n⌔︙ الامر  •  `.بايو وقتي`\n⌔︙ الاستخدام •  فقط اكتب الامر لعرض تاريخ يتغير مع النبذة \n\n\n⌔︙ اوامر الايقاف  •\n⌔︙ `.انهاء اسم وقتي`  • لايقاف الاسم الوقتي\n⌔︙`.انهاء بايو وقتي`  • لايقاف البايو الوقتي\n⌔︙ `.انهاء الصورة الوقتية`  • لايقاف الصورة الوقتية\n\n⌔︙ قـناة الـسورس  •\n⌔︙ @JMTHON")

@borg.on(admin_cmd("م19"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙  اوامر هيروكو والفارات \n\n⌔︙ الامـر  •  `.استخدامي`\n⌔︙ الاستخدام  • ارسل الامر فقط لعرض مدة  استخدام للسورس والساعات المتبقية\n\n⌔︙ الامـر  •  `.الدخول`\n⌔︙ الاستخدام •  فقط اكتب الامر لعرض اخر 100 سطر من تطبيق هيروكو الي نصبت عليه\n\n⌔︙ الامـر •  `.set var`  <متغير الفار>  <القيمة>\n⌔︙ الاستخدام • يستخدم هذا الامر لوصع فار في هيروكو باستخدام البوت فقط شاهد متغيرات الفارات على قناة المساعدة\n ⌔︙ مثـال  •  `.set var TZ Asia/Baghdad `  <بعد استخدام الامر راح يتوقف البوت 2 د> \n\n⌔︙ الامـر •  `.del var <متغير الفار>`\n⌔︙ الاستخدام • يستخدم لحذف فار من التطبيق انتبه توجد فارات اذا حذفتها يتوقف البوت\n⌔︙ مثـال  •  `.del var DIGITAL_PIC`  <سيقوم بحذف فار الصورة> \n\n⌔︙ CH : @JMTHON")

        
@borg.on(admin_cmd("م20"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ الاوامر الارسال \n⌔︙ ملاحظة • لاستخدام امر نقل الملكية تحتاج لوضع TG_2STEP_VERIFICATION_CODE و معه رمز حسابك في الفارات \n\n⌔︙ الامـر  • `.ملكية` \n⌔︙ الاستخـدام  • يجب عليك كتابة التمر في القناه التي تريد تحويلها لشخص وبكتابه الامر مع معرف الشخص  \n\n⌔︙ الامـر  •  `.لستة`\n⌔︙ الاستخـدام • يقوم بصنع لستة شفافة لمنشور معين شاهد الشرح اضغط هنا \n\n⌔︙ الامـر • `.الوقت`\n⌔︙ الاستخـدام • فقط ارسل الامر وسيعرض لـك توقيت بلدك على ملصق\n\n⌔︙ الامـر  •  `.تحذير` <سبب> \n⌔︙ الاستخـدام  • بالرد على الشخص ليقوم بتحذيره \n\n⌔︙ الامـر • `.التحذيرات` \n⌔︙ الاستخـدام  • بالرد على الشخص ليقوم باظهار تحذيراته  \n\n⌔︙ الامـر • `.حذف التحذيرات`  <بالرد>\n⌔︙ الاستخـدام  • بالرد على الشخص لحذف تحذيراته \n\n⌔︙ الامـر • `.تطبيق` <اسم تطبيق>\n⌔︙ الاستخـدام • كتابة الامر مع اسم تطبيق او لعبه وسيعطيك تفاصيلها ورابط تنزيل من سوق بلي \n\n⌔︙ Ch  - @JMTHON")

@borg.on(admin_cmd("م21"))
async def _(event):  # كتابة الملف بواسطه  : @RRRD7
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("قـريبا خـاص بـسورس جـمثون")

@borg.on(admin_cmd("م22"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر الملصقات \n\n⌔︙الامر  • `.ملصق`  <بالرد>\n⌔︙  الاستخدام 𖥻 بالرد على الملصق لأخذه وعمل حزمه واضافته به\n\n⌔︙ الامر  • `.حزمة`  <بالرد>\n⌔︙ الاستخدام • بالرد على الملصق لنسخ الحزمه كاملـة\n\n⌔︙ الامر • `.معلومات_الملصق`  <بالرد>\n⌔︙ الاستخدام •  بالرد على الملصق لعرض معلومات الحزمة\n\n⌔︙ CH - @JMTHON")

@borg.on(admin_cmd("م23"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامـر مساعـدة \n\n⌔︙ الأمـر  • موقع <المڪـان> \n ⌔︙ للحصول على خريطه المكان وارساله لك\n\n ⌔︙ الامر  • `.صوره`  <بالرد> \n⌔︙ الاستخدام  • بالرد على الشخص للحصول على صورة حسابه الشخصيه واذا تريد جميع صور حسابه قم بالرد عليه بـ `.صوره كلها` \n\n⌔︙ الأمـر  • `.سرعة الانترنت` \n⌔︙ الاستخدام • ارسل الامر لقياس سرعة الانترنت \n\n⌔︙ الأمـر  •  `.حساب` \n⌔︙ الاستخدام  • كتابة الامر مع معادلة رياضيات وسيقوم بحلها وارسالها لك \n\n⌔︙ الأمـر  •  `.تاريخ` \n⌔︙ الاستخدام  • بالرد على الشخص او كتابة معرفه مه الامر لعرض سجل اسماء حسابه \n\n⌔︙ الأمـر • `.الوقت` \n⌔︙ الاستخدام • لعرض الوقت على شكل ملصق \n\n⌔︙ الأمـر • `.وقت` \n⌔︙ الاستخدام • لعرص الوقت والتاربخ على شكل كتابة \n\n⌔︙ الأمـر • `.صلاة`\n⌔︙ الاستخدام • اكتب الامر مع اسم محافظتك باللغه الانكليزية للحصول على اوقات الصلاة\n\n⌔︙ الامـر  •  `.كورونا  <اسم الدولة انكليزي>\n⌔︙ الاستخـدام  • بعرض تفاصيل عن الدولة المعينة لمرض فايروس كورونا اكتب الامر مع اسم الدولة باللغه الانكليزيه فقط\n⌔︙ مثـال  •  `.كورونا Iraq`\n\n⌔︙ الامر  •  `.مؤقت`  <الوقت > <النص>\n⌔︙ الاستـخدام • يقوم بأرسال رسالة مؤقتة وحذفها بعد وقت معين\n⌔︙ مثـال  •  `.مؤقت 5 جمثون`  \n\n⌔︙ CH : @JMTHON")
        
@borg.on(admin_cmd("م24"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر الروابط\n\n⌔︙ الامر • .دنس  <رابط>\n⌔︙ استخدامه • لكشف معلومات نظام دومين موقع معين اكتب الامر مع الرابط\n\n⌔︙ الامر • .مصغر <بالرد>\n⌔︙ استخدامه  • بالرد على الرابط او وضع الرابط مع الامر ليقوم بتصغيره \n\n⌔︙ الامر • `.رابط_مخفي `  <بالرد>\n⌔︙ استخدامه  • بالرد على الرابط لاخفاء الرابط وجعله في مسافه معينه جرب الامر بنفسك\n\n⌔︙CH :  @JMTHON")

@borg.on(admin_cmd("م25"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر التخصيص \n\n⌔︙ الامر  • `.تخصيص pmpermit` <بالرد>\n⌔︙  الاستخدام  • بالرد على الرسالة التي تريد وضعها رسالة تحذيرات لامر حماية الخاص\n\n ⌔︙ الامر • `.تخصيص pmblock` <بالرد> \n⌔︙ الاستخدام  • يستخدم هذا الامر لوضع رسالة الحظر التي ترسل بعدما الشخص يقوم بتكرار الرسائل في الخاص قم بالرد على الرسالة التي تريد وضعها بالامر \n\n⌔︙ الامر • `.تخصيص startmsg` \n⌔︙ استخدامه • بالرد على الرسالة التي تريدها تظهر بعدما الشخص يشغل بوتك \n\n⌔︙ CH- @JMTHON") 
       
@borg.on(admin_cmd("م26"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("⌔︙ اوامر التكرار والسبام\n\n⌔︙ الامـر  •  .كرر  <عدد التكرار>  <بالرد> \n⌔︙ الاستخدام • يقوم بعمل تكرار لرسالة او صورة او اي شي فقط قم بالرد عليه بـ  ~  .كرر  <عدد التكرار>  <بالرد> \n⌔︙ مثـال •  بالـرد على صورة  .كرر 10  \n\n⌔︙ الامـر  •  `.تكرار الملصق` <بالرد على حزمه> \n⌔︙ الاستخدام  • بالرد على ملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها\n\n⌔︙ الامـر   •  `.سبام`  <كلمه> \n⌔︙ الاستخدام  • يقوم بتفصيخ احرف الكلمه وارسالها\n⌔︙ مثـال  •  `.سبام جمثون`\n\n⌔︙ الامـر  •  `.وسبام`  <جمله>\n⌔︙ الاستخدام •  كتابة الامر مع نص معين يقوم بتفصيخ الجمله كلمه كلمه وارسالها\n⌔︙ مثال  •  .وسبام سورس جمثون العربي\n\n⌔︙ الامـر  •  `.مكرر`  <وقت> <عدد تكرار> <بالرد >\n⌔︙ الاستخدام •  بالرد على نص او صورة او اي شي يقوم بالتكرار  مع وقت معين \n⌔︙ مثـال  •  بالـرد على نص { .مكرر 10 2 } عندها سترسل 10 رسائل نصية {النص الي رديت عليه } بفاصل ثانيتين بين كل رسالة \n\n ⌔︙ CH - @JMTHON")
